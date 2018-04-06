from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)
from .views import RecoverView, OrdinaryUserViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register(r'^ordinary_user', OrdinaryUserViewSet)

urlpatterns = ROUTER.urls

urlpatterns += [
    url(r'authenticate/$', obtain_jwt_token),
    url(r'refresh/$', refresh_jwt_token),
    url(r'password/$', RecoverView.as_view(), name='password'),
]
