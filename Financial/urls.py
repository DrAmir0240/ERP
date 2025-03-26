from django.urls import path
from .views import OrderCreateAPIView, PaymentCreateAPIView

urlpatterns = [
    path('order/create/', OrderCreateAPIView.as_view(), name='create-order'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='create-payment'),
]
