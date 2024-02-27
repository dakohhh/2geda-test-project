import threading
from authentication.auth import Auth
from client import CustomResponse
from rest_framework.request import Request
from rest_framework.views import APIView
from repository.user import UserRepository
from .serializers import UserSerializer, LoginSerializer
from utils.mail import send_welcome_email
from rest_framework.exceptions import AuthenticationFailed
import rest_framework.status as status


auth = Auth()


class Signup(APIView):

    def post(self, request: Request):

        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        email = serializer.validated_data["email"]
        firstname = serializer.validated_data["firstname"]
        lastname = serializer.validated_data["lastname"]

        thread = threading.Thread(
            target=send_welcome_email,
            args=(
                firstname,
                lastname,
                email,
            ),
        )

        thread.start()

        return CustomResponse(
            serializer.data, "created user successfully", status=status.HTTP_201_CREATED
        )


class Login(APIView):

    def post(self, request: Request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            token = auth.authenticate_user(email, password)

            context = {"token": token}

        return CustomResponse(context, "login successfull")
