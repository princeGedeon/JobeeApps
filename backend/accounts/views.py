from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.serializers import SignUpSerializer

from accounts.serializers import UserSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentUser(request):

    user=UserSerializer(request.user)

    return Response(user.data)

@swagger_auto_schema(query_serializer=SignUpSerializer,method='POST')
@api_view(['POST'])
def register(request):
    data=request.data

    user=SignUpSerializer(data=data)

    if user.is_valid():

        if not User.objects.filter(username=data['email']).exists():

            user=User.objects.create(
               first_name=data['first_name'],
               last_name=data['last_name'],
               username=data['email'],
               email=data['email'],
               password=make_password(data['password'])
           )
            return Response({
                "message":"User registered",

            },
            status=status.HTTP_201_CREATED)
        else:
            return Response(
                {
                    'error':"User already exists"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(user.errors)