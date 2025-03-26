from django.urls import path

from Users import views

urlpatterns = [
    path('customer/create/', views.CustomerCreateAPIView.as_view(), name='create-customer'),
    path('driver/create/', views.DriverCreateAPIView.as_view(), name='create-driver'),
    path('manager/create/', views.ManagerCreateAPIView.as_view(), name='create-manager'),
    path('main-manager/create/', views.MainManagerCreateAPIView.as_view(), name='create-main-manager'),
    path('drivers/list/', views.DriverListAPIView.as_view(), name='-drivers-list'),
    path('managers/list/', views.ManagerListAPIView.as_view(), name='managers-list'),
    path('customers/list/', views.CustomerListAPIView.as_view(), name='customers-list'),
    path('drivers/profile/', views.DriverProfileView.as_view(), name='driver-profile'),
    path('managers/profile/', views.ManagerProfileView.as_view(), name='manager-profile'),
    path('main_manager/profile/', views.MainManagerProfileView.as_view(), name='main-manager-'),

]
