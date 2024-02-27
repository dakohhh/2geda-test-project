import typing
from main.models import User


class UserRepository:

    @staticmethod
    def get_user_by_email(email: str) -> typing.Union[User, None]:

        query = User.objects.filter(email=email).first()

        return query
