from django.urls import path
from user.views import UserLoginView
from django.contrib.auth.views import LogoutView
from user.views import SignUpView

app_name = "user"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/ ", LogoutView.as_view(), name="logout"),
    path("register/", SignUpView.as_view(), name="register"),
]
