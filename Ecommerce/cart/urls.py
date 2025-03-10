from django.urls import path
from . import views

urlpatterns =[
    path("",views.CartListView.as_view(),name="cart"),
    path("add/<int:product_id>",views.CartCreateView.as_view(),name='cart_add'),
    path("update/<int:pk>",views.CartUpdateView.as_view(),name="update_item"),
    path("delete/<int:pk>",views.CartDeleteView.as_view(),name="delete_item"),
]