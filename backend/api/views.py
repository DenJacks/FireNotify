from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate

from users.models import User
from .models import Activity
from .serializers import UserSerializer, ActivitySerializer


# =========================================================
# GET ALL USERS
# =========================================================

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# =========================================================
# REGISTER
# =========================================================

class RegisterView(APIView):

    def post(self, request):

        first_name = request.data.get("first_name", "").strip()
        last_name = request.data.get("last_name", "").strip()
        email = request.data.get("email", "").strip().lower()
        password = request.data.get("password", "")

        # ---------------------------------------------
        # Validate required fields
        # ---------------------------------------------

        if not first_name or not last_name:
            return Response(
                {
                    "error": "First name and last name are required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not email:
            return Response(
                {
                    "error": "Email is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not password:
            return Response(
                {
                    "error": "Password is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ---------------------------------------------
        # Password length
        # ---------------------------------------------

        if len(password) < 8:
            return Response(
                {
                    "error": "Password must be at least 8 characters long."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ---------------------------------------------
        # Check duplicate email
        # ---------------------------------------------

        if User.objects.filter(email=email).exists():
            return Response(
                {
                    "error": "This email is already registered."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ---------------------------------------------
        # Create username
        # ---------------------------------------------

        username = email.split("@")[0]

        original_username = username
        counter = 1

        while User.objects.filter(username=username).exists():
            username = f"{original_username}{counter}"
            counter += 1

        # ---------------------------------------------
        # Create user
        # ---------------------------------------------

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role="PERSONNEL"
        )

        # ---------------------------------------------
        # Return created user
        # ---------------------------------------------

        serializer = UserSerializer(user)

        return Response(
            {
                "message": "Registration successful.",
                "user": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


# =========================================================
# LOGIN
# =========================================================

class LoginView(APIView):

    def post(self, request):

        email = request.data.get("email", "").strip().lower()
        password = request.data.get("password", "")

        # ---------------------------------------------
        # Validate
        # ---------------------------------------------

        if not email or not password:
            return Response(
                {
                    "error": "Email and password are required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ---------------------------------------------
        # Find user by email
        # ---------------------------------------------

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {
                    "error": "Invalid email or password."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        # ---------------------------------------------
        # Authenticate password through Django
        # ---------------------------------------------

        authenticated_user = authenticate(
            username=user.username,
            password=password
        )

        if authenticated_user is None:
            return Response(
                {
                    "error": "Invalid email or password."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        # ---------------------------------------------
        # Check active account
        # ---------------------------------------------

        if not user.is_active:
            return Response(
                {
                    "error": "This account is inactive."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        # ---------------------------------------------
        # Successful login
        # ---------------------------------------------

        serializer = UserSerializer(user)

        return Response(
            {
                "message": "Login successful.",
                "user": serializer.data
            },
            status=status.HTTP_200_OK
        )


    # =========================================================
# ACTIVITIES
# =========================================================

class ActivityListCreateView(generics.ListCreateAPIView):

    queryset = Activity.objects.all().order_by("-created_at")
    serializer_class = ActivitySerializer