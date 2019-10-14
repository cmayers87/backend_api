from rest_framework import routers
from .api import Model1ViewSet, Model2ViewSet, Model3ViewSet


router = routers.DefaultRouter()
router.register('api/model1', Model1ViewSet, 'model1')
router.register('api/model2', Model2ViewSet, 'model2')
router.register('api/model3', Model3ViewSet, 'model3')

urlpatterns = router.urls
