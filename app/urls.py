from django.urls import path

from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('category/<slug:val>/',views.CategoryView.as_view(),name='category'),
    path('product-details/<int:pk>/',views.product_details,name='product_details'),
]