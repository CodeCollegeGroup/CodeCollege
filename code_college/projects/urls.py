from rest_framework import routers
from projects.views import ProjectViewSet, ProjectImageViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register(r'^projects', ProjectViewSet)
ROUTER.register(r'^projects_images', ProjectImageViewSet)

urlpatterns = ROUTER.urls
