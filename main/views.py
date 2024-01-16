from django.contrib.auth.views import get_user_model
from django.db import transaction
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.permission import IsAdminPermission
from .models import Product
from .serializers import ProductSerializerForPost, ProductSerializer

User = get_user_model()


class AddProductAPIView(GenericAPIView):
    permission_classes = (IsAdminPermission,)
    serializer_class = ProductSerializerForPost

    def post(self, request, format=None):  # noqa
        mutable_data = request.data.copy()
        mutable_data['user_id'] = request.user.id
        product_serializer = ProductSerializerForPost(data=mutable_data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(product_serializer.data)


def get(self, request, *args, **kwargs):
    product = self.get_object()
    with transaction.atomic():
        product.viewed += 1
        product.save()
    return Response({"message": "Product viewed successfully"})


class ProductLictAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class UpdateProductDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAdminPermission,)
