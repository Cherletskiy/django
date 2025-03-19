from rest_framework import serializers

from main.models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    # реализуйте сериализацию объектов модели Book
    orders_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"

    # решил заменить метод to_representation на order_set.count(), в данном случае этот способ проще, т.к. требуется всего создать одно доп. поле
    def get_orders_count(self, obj):
        return obj.order_set.count()


class OrderSerializer(serializers.ModelSerializer):
    # добавьте поля модели Order
    class Meta:
        model = Order
        fields = "__all__"

    #доп задание
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        books = instance.books.all()
        serializer = BookSerializer(books, many=True)
        books_data = serializer.data

        representation['books'] = books_data
        return representation
