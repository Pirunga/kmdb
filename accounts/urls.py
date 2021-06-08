from django.urls import path
from accounts.views import AccountCreateView, LoginView


urlpatterns = [
    path("accounts/", AccountCreateView.as_view()),
    path("login/", LoginView.as_view()),
]
