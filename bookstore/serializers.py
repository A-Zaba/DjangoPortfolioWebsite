from rest_framework import serializers
from .models import Book, Review


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=75)
    isbn = serializers.IntegerField(required=False)
    publish_date = serializers.DateField(required=False)

class ReviewSerializer(serializers.ModelSerializer):
    pass
    book = serializers.ReadOnlyField(source ="book.")