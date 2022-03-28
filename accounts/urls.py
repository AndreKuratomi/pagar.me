from django.urls import path
from accounts.views import UserView, LoginUserView

urlpatterns = [
    path('accounts/', UserView.as_view()),
    path('login/', LoginUserView.as_view())
]
