from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('language', LanguageViewSet, basename='language')
router.register('keywords', KeywordViewSet, basename='keywords')

urlpatterns = router.urls
