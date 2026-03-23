from django.urls import path

from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('category/<slug:val>/',views.CategoryView.as_view(),name='category'),
    path('product-details/<int:pk>/',views.product_details,name='product_details'),

    #cart
    path('add-to-cart/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.show_cart,name='show_cart'),
    path('pluscart/<int:pid>/',views.plus_cart,name='plus_cart'),
    path('minuscart/<int:pid>/',views.minus_cart,name='minus_cart'),
    path('removefromcart/<int:pid>',views.remove_from_cart,name='remove_from_cart'),

    path('checkout/',views.checkout,name='checkout'),
    path('payment_gateway/',views.payment_gateway,name='payment_gateway'),
    path('orderplaced/',views.orderplaced,name='orderplaced'),
    path('orders/',views.orders,name='orders'),

]