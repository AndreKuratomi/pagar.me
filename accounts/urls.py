from django.urls import path
from accounts.views import UserView, UserByIdView, LoginUserView

urlpatterns = [
    path('accounts/', UserView.as_view()),
    path('accounts/<str:user_id>/', UserByIdView.as_view()),
    path('login/', LoginUserView.as_view())
]
