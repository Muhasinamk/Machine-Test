from django.urls import path


from .views import FlowerList, FlowerDetail, cart, add_to_cart, remove_from_cart

urlpatterns=[
path('flowerlist/', FlowerList.as_view(), name='flowers'),
    path('flowerdetail/<int:pk>/', FlowerDetail.as_view(), name='flowerdetail'),

path('cart/', cart, name='mycart'),
    path('cart/add/<int:flower_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:flower_id>/', remove_from_cart, name='remove_from_cart'),


]