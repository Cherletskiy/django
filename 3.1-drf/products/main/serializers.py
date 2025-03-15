from rest_framework import serializers
from main.models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    class Meta:
        model = Review
        fields = ['id', 'product', 'text', 'mark', 'created_at']
        read_only_fields = ['id', 'created_at']


class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    reviews = serializers.SerializerMethodField()

    def get_reviews(self, obj):
        reviews = obj.comments.all()
        return [{"text": review.text, "mark": review.mark} for review in reviews]

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'reviews']
