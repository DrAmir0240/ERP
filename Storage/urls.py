from django.urls import path
from .views import CargoCreateAPIView

urlpatterns = [
    path('cargo/create/', CargoCreateAPIView.as_view(), name='create-cargo'),
]
