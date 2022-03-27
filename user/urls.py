from django.urls import path
from user.views import UserView, LoginUserView

urlpatterns = [
    path('accounts/', UserView.as_view()),
    path('login/', LoginUserView.as_view())
]
