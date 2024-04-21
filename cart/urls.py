from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:cart_id>',views.checkout, name='checkout'),
    path('paymentdone/<int:cart_id>',views.payment_done, name='payment_done'),
    path('booking/<int:car_id>',views.car_booking, name='car_booking'),
    path('create-checkout-session',views.create_checkout_session, name='create_checkout_session'),
    path('order',views.order, name='order'),
    path('',views.shop_cart, name='shop_cart'),
    path('save_booking/', views.save_booking, name='save_booking'),
    path('apply-coupon', views.apply_coupon, name='apply_coupon'), 
    ] 