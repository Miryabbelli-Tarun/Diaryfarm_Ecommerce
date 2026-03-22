from django.urls import path

from accounts import views


urlpatterns = [
    path('customer-register/',views.customer_register,name='customer_register'),
    path('customer_login/',views.customer_login,name='customer_login'),
    path('customer-logout/',views.customer_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('address-edit/<int:pk>/',views.edit_address,name='edit_address'),
    path('address_delete/<int:pk>/',views.delete_address,name='delete_address'),
    path('change-password/',views.change_password,name='change_password'),
]