from django.urls import path
from fees.views import FeeView, FeeByIdView

urlpatterns = [
    path('fee/', FeeView.as_view()),
    path('fee/<str:fee_id>', FeeByIdView.as_view())
]
