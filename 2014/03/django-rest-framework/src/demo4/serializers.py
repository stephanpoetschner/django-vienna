from .models import Book, BookReview
from rest_framework import serializers

class BookReviewSerializer(serializers.ModelSerializer):
    created_by = serializers.Field(source='created_by.username')

    class Meta:
        model = BookReview
        fields = ('review', 'created_by', 'created_at', )

class LeanBookSerializer(serializers.HyperlinkedModelSerializer):
    thumb = serializers.Field(source='get_image_thumb')

    class Meta:
        model = Book
        fields = ('url', 'title', 'price_net', 'thumb', )

class BookSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(source='title')
    authors = serializers.Field(source='get_author_names')
    created_by = serializers.Field(source='created_by.username')

    reviews = BookReviewSerializer(source='book_reviews', many=True)

    thumb = serializers.Field(source='get_image_thumb')
    main = serializers.Field(source='get_image_main')

    class Meta:
        model = Book
        fields = ('url', 'title', 'abstract', 'price_net', 'authors',
                  'created_by', 'reviews', 'thumb', 'main', )
