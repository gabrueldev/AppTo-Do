from django.contrib.auth.models import User
from .serializers import cadaster_serializer, login_serializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class cadaster_view(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = cadaster_serializer
    permission_classes = []

class login_view(TokenObtainPairView):
    serializer_class = login_serializer

class edit_view(UpdateAPIView):
    queryset           = User.objects.all()
    serializer_class   = cadaster_serializer
    lookup_field       = "username"
    permission_classes = [IsAuthenticated, IsOwner]

class delete_view(DestroyAPIView):
    queryset           = User.objects.all()
    serializer_class   = cadaster_serializer
    lookup_field       = "username"
    permission_classes = [IsAuthenticated, IsOwner]