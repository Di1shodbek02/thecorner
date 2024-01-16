from django.urls import path

from main.views import AddProductAPIView, ProductLictAPIView, UpdateProductDestroyAPIView

urlpatterns = [
    path('add-product', AddProductAPIView.as_view(), name='add_product'),
    path('product-list', ProductLictAPIView.as_view(), name='product_list'),
    path('update-product', UpdateProductDestroyAPIView.as_view(), name='update_product'),
]
