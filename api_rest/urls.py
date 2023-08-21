from rest_framework import routers
from django.urls import path, include
from . import resources


router = routers.DefaultRouter(trailing_slash=True)

router.register('user', resources.UserResource, 'user')

urlpatterns = [
    path('', include(router.urls))
]
