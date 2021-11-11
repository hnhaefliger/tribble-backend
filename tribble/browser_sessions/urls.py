from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('session', SessionViewSet, basename='session')

urlpatterns = router.urls
