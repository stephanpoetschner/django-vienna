from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(source='title')
    authors = serializers.Field(source='get_author_names')
    created_by = serializers.Field(source='created_by.username')

    class Meta:
        model = Book
        fields = ('url',
                  'title',
                  'abstract',
                  'price_net',
                  'authors',
                  'created_by')
