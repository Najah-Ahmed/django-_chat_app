from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Front_Page,SignUpUser
urlpatterns =[
  path("",Front_Page, name="frontpage"),
  path("signup/",SignUpUser, name="signup"),
  path("login/", auth_views.LoginView.as_view(template_name="core/login.html"),name="login"),
  path("logout/" ,auth_views.LogoutView.as_view(
    # template_name="core/logout.html"
    ),name="logout"),
]