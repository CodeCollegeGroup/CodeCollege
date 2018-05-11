from rest_framework import routers
from projects.views import ProjectViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register(r'^projects', ProjectViewSet)

urlpatterns = ROUTER.urls
