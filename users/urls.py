from django.urls import path
from django.conf.urls import url
from .views import login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_view, name="login"),
    path('login/', login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]