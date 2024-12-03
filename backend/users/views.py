from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializers import CustomUserSerializer
from .serializers import ProfileSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        refresh = RefreshToken.for_user(user)

        return Response({"refresh": str(refresh), "access": str(refresh.access_token)})


class RegisterView(APIView):
    def post(self, request):
        request.data["tenant"] = request.tenant.pk
        request.data["password"] = make_password(request.data.get("password"))
        request.data["gln"] = (
            request.data.get("gln") if request.data.get("gln") != "" else None
        )
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Kayıt başarılı."}, status=status.HTTP_201_CREATED
            )
        else:
            if serializer.errors.get("email"):
                if (
                    str(serializer.errors.get("email")[0])
                    == "user with this email address already exists."
                ):
                    return Response(
                        {"error": "E-posta zaten kayıtlı."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            if serializer.errors.get("gln"):
                if (
                    str(serializer.errors.get("gln")[0])
                    == "user with this gln already exists."
                ):
                    return Response(
                        {"error": "GLN zaten kayıtlı."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request) -> Response:
    try:
        user_email = request.data['email']
        serializer = ProfileSerializer(user_email)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({"error": "Kullanıcı bulunamadı."}, status=status.HTTP_404_NOT_FOUND)