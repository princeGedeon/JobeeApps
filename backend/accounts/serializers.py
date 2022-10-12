from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class SignUpSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name',"last_name","email","password"]

        extra_kwargs={
            'first_name':{'required':True,'allow_blank':False},
            'last_name': {'required': True, 'allow_blank': False},
            'email': {'required': True, 'allow_blank': False},
            'password': {'required': True, 'allow_blank': False,'min_length':6},
        }


class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['last_name','first_name',"email","username"]