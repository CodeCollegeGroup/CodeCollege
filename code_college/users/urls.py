from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)
from .models import ProjectOwner, ProjectContributes, CommentsOwner
from .views import RecoverView, OrdinaryUserViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register(r'^ordinary_user', OrdinaryUserViewSet)

urlpatterns = ROUTER.urls  # pylint: disable=invalid-name

urlpatterns += [
    url(r'authenticate/$', obtain_jwt_token),
    url(r'refresh/$', refresh_jwt_token),
    url(r'password/$', RecoverView.as_view(), name='password'),
    url(r'myprojects/$', ProjectOwner.get_result),
    url(r'contributes/$', ProjectContributes.get_result),
    url(r'mycomments/$', CommentsOwner.get_result),
]
