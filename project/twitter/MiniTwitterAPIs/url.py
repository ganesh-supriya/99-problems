from django.contrib import admin
from django.urls import path
from .views import  LoginView,LogoutView, AllUsersView,MyProfile,MyProfileUpdate,RegisterView
from rest_framework.authtoken import views
urlpatterns = [

     path('register/',RegisterView.as_view()),
     path('login/',LoginView.as_view()),
     path('allusers/',AllUsersView.as_view()),
     path('logout/',LogoutView.as_view()),
     path('myprofile/<int:pk>/',MyProfile.as_view()),
     path('updatemyprofile/<int:id>/',MyProfileUpdate.as_view()),
     # path('timeLine/', ),               #must use lowercase
     # path('users/', ),
     # path('SearchUser/<name>/', ),
     # path('user-profile/<int:id>/', ),
     # path('followers-following/', ),
     # path('tweets/', ),
     # path('TweetLikes/<int:id>', ),
     # path('TweetComments/<int:id>', ),
     # path('logout/', )

]