import os
import jwt
import pydantic
from main.models import User
from utils.validation import Token
from datetime import timedelta, datetime
from repository.user import UserRepository
from rest_framework.exceptions import (
    AuthenticationFailed,
    ValidationError,
    NotAuthenticated,
)


SECRET_KEY = str(os.getenv("SECRET_KEY"))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = timedelta(days=30)


class AuthToken:
    def __init__(self):
        self.secret_key = SECRET_KEY
        self.algorithm = ALGORITHM
        self.access_token_expire = ACCESS_TOKEN_EXPIRE_MINUTES

    def create_access_token(self, user: User):
        token = jwt.encode(
            {"id": user.id, "exp": datetime.now() + self.access_token_expire},
            SECRET_KEY,
        )

        return token

    def verify_access_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])

            instance = Token(**payload)

            if instance.get_expiry_time() < datetime.now():
                raise NotAuthenticated("session token has expired")

            return instance

        except jwt.PyJWTError as e:
            raise ValidationError(str(e))

        except pydantic.ValidationError as e:
            raise ValidationError("invalid access token")


class Auth:
    def __init__(self):
        self.auth_token = AuthToken()

    def authenticate_user(self, email: str, password: str):

        user = UserRepository.get_user_by_email(email)

        print(user.firstname, user.lastname)

        if user is None or not user.check_password(password):
            raise AuthenticationFailed("incorrect email or password")

        access_token = self.auth_token.create_access_token(user)

        return access_token
