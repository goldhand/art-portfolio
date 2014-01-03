try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from rest_framework.routers import DefaultRouter

from imagestore.views import ImageViewSet

router = DefaultRouter()
router.register(r'images', ImageViewSet)

urlpatterns = patterns('apiroot.views',
                       url(r'^', include(router.urls)),
                       )
