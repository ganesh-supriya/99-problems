from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework.filters import SearchFilter
from .models import UserProfile,User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from django.conf import settings
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        users = User.objects.filter(email=email).first()


        if users is None:
            raise AuthenticationFailed('user not found')

        if not users.check_password(password):
            raise AuthenticationFailed('invalid password')

        token, created = Token.objects.get_or_create(user=users)

        return Response({'token': token.key})

        return Response({
            'message': 'success'
        })

# class AllUsersView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#    # permission_classes = [IsAuthenticated,]
#
#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
class AllUsersView(ListAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields=['name']


class MyProfile(generics.ListCreateAPIView):
    queryset = UserProfile.objects.filter()
    serializer_class = UserProfileSerializer


class MyProfileUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile
    lookup_field = 'id'
    serializer_class = UserProfileSerializer



class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.data = {
            'message': 'success'
        }
        return response
