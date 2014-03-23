from django.contrib import admin
from .models import Book, Author, BookAuthors, BookReview

class BookAuthorsInline(admin.TabularInline):
    #fields = ('first_name', 'last_name', )
    readonly_fields = ('order',)
    model = BookAuthors
    extra = 1

class BookReviewInline(admin.TabularInline):
    model = BookReview
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [BookAuthorsInline, BookReviewInline]

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
