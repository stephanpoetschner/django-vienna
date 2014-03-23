from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for my very sophisticated book model
    """
    # Demo #4
    queryset = Book.objects.all().prefetch_related('authors', 'created_by')
    serializer_class = BookSerializer
