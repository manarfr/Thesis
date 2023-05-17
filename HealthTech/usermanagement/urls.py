from django.urls import path
from . import views
from .views import UserLoginView, ProfileView

urlpatterns = [
   path("signup/", views.signup, name="singup"),
   path("home/", views.home, name="home"),
   path("login/", UserLoginView.as_view() , name="login"),
   path("profile/", ProfileView.as_view(), name="profile"),

]