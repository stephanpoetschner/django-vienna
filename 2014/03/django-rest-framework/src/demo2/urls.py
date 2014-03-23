from django.conf.urls import patterns, url, include
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
