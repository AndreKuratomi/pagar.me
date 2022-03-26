from django.urls import path
from user.views import UserView

urlpatterns = [
    path('accounts/', UserView.as_view())
]