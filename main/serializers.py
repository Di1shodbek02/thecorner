from rest_framework.serializers import ModelSerializer

from main.models import Product


class ProductSerializerForPost(ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'images', 'author', 'video_url',)


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
