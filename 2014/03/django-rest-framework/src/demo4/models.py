from django.db import models
from django.contrib.auth.models import User
from .mixins import ImageMixin

class Author(models.Model):
    """
    Author of a Book
    """
    first_name = models.CharField(
        max_length=40,
        verbose_name=u'First Name')

    last_name = models.CharField(
        max_length=40,
        verbose_name=u'Last Name')

    def __unicode__(self):
        return u' '.join([self.first_name, self.last_name])

    class Meta:
        verbose_name = u'Author'
        verbose_name_plural = u'Authors'
        ordering = ('last_name', )

class BookAuthors(models.Model):
    author = models.ForeignKey('Author')
    book = models.ForeignKey('Book')
    order = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        """
        automatically calculate the order before saving (if order is not set)
        """
        if self.order is None:
            count = BookAuthors.objects.filter(book__pk=self.book.pk).count()
            self.order = count
        super(BookAuthors, self).save(*args, **kwargs)

    class Meta:
        ordering = ('order', )

class Book(ImageMixin, models.Model):
    """
    My first book model
    """
    title = models.CharField(
        max_length=255,
        verbose_name=u'Book Title')

    abstract = models.TextField(
        verbose_name=u'Abstract')

    price_net = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name=u'Price Net')

    authors = models.ManyToManyField(
        Author,
        through=BookAuthors,
        related_name='book_authors',
        verbose_name=u'Authors')

    created_by = models.ForeignKey(
        User,
        related_name=u'demo4_book_created_by',
        verbose_name=u'Created by')

    def get_image_alt(self):
        return u'authors: %s' % self.get_author_names

    def get_image_title(self):
        return self.title

    def get_author_names(self):
        """
        returns a list of all author names as string
        e.g. "Kai Johnson, Mark Wahlberg, ..."
        """
        return u', '.join([unicode(a) for a in self.authors.all()])

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Book'
        verbose_name_plural = u'Books'
        ordering = ('title', )

class BookReview(models.Model):
    """
    a book review
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=u'Review created at')

    created_by = models.ForeignKey(
        User,
        related_name='review_user',
        verbose_name=u'Review created by')

    book = models.ForeignKey(
        Book,
        related_name='book_reviews',
        verbose_name=u'Book')

    review = models.TextField(
        verbose_name=u'Review Text')

    def __unicode__(self):
        return u'Review of book "%(book)s" (created by %(user)s)' % {
            'book': self.book,
            'user': self.created_by,
        }

    class Meta:
        verbose_name = u'Book Review'
        verbose_name_plural = u'Book Reviews'
        ordering = ('-created_at', )
