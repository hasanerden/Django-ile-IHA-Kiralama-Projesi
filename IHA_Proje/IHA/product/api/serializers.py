from rest_framework import serializers
from product.models import Category



class CategorySerializer(serializers.ModelSerializer):

    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='categories',
    )

    class Meta:
        model = Category
        fields = '__all__'