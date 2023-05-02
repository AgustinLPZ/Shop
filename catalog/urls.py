from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('my_cart/', views.my_cart, name='my_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_success/', views.order_success, name='order_success'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),

]
