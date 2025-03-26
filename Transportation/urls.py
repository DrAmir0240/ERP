from django.urls import path
from .views import TransportCarCreateAPIView, TransportCarListAPIView

urlpatterns = [
    path('create/', TransportCarCreateAPIView.as_view(), name='create-transport-car'),
    path('list/', TransportCarListAPIView.as_view(), name='list-transport-cars'),
]