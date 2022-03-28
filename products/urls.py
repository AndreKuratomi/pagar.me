from django.urls import path
from products.views import ProductView, ProductByIdView, ProductBySellerIdView

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<str:product_id>/', ProductByIdView.as_view()),
    path('products/seller/<str:seller_id>/', ProductBySellerIdView.as_view())
]
