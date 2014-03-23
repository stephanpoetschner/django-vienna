from django.db import models

class Book(models.Model):
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

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Book'
        verbose_name_plural = u'Books'
        ordering = ('title', )
