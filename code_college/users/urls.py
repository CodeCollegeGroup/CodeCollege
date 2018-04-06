from django.conf.urls import url
from dr_auth.views import RecoverView
from rest_framework import routers
from users.views import OrdinaryUserViewSet
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)

urlpatterns = [
    url(r'^$', obtain_jwt_token),
    url(r'^refresh/$', refresh_jwt_token),
    url(r'^password/$', RecoverView.as_view(), name='password'),
]

ROUTER = routers.DefaultRouter()
ROUTER.register(r'^ordinary_user', OrdinaryUserViewSet)

urlpatterns += ROUTER.urls
