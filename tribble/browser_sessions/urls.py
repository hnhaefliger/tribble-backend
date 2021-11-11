from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('', SessionViewSet, basename='session')

urlpatterns = router.urls
