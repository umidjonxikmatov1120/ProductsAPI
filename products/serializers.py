from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from products.models import ProductsModel

class ProductsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = ('id', 'title', 'articul', 'cloth', 'color', 'image', 'size', 'material')


class ProductsValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    articul = serializers.CharField()
    cloth = serializers.CharField()
    color = serializers.CharField()
    image = serializers.URLField()
    size = serializers.CharField()
    material = serializers.CharField()

    def validate(self, data):
        title = data.get('title', None)

        if ProductsModel.objects.filter(title=title).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Bunday nom bor.Iltimos boshqa nom kiriting!"
                }
            )

        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Mahsulotni nomi harflardan tashkil topgan bo'lshi kerak !"
                }
            )
        return data


    def validate_price(self, price):
        if 0 < price < 10_000_000_000:
            raise ValueError(
                {
                    'status': False,
                    'message': "Narx noto'g'ri kiritilgan"
                }
            )