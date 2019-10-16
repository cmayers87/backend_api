from django.urls import path, include
from rest_framework import routers
from .api import modelapi, funcapi
from . import views


router = routers.DefaultRouter()
router.register('api/model1', modelapi.Model1ViewSet, 'model1')
router.register('api/model2', modelapi.Model2ViewSet, 'model2')
router.register('api/model3', modelapi.Model3ViewSet, 'model3')

urlpatterns = [
    path('', include(router.urls)),
    path('query', funcapi.query),
    path('func1', funcapi.func1),
    path('func2', funcapi.func2)
]
