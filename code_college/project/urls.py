from rest_framework import routers
from project.views import ProjectViewSet 

ROUTER = routers.DefaultRouter()
ROUTER.register(r'^project', ProjectViewSet)

urlpatterns = ROUTER.urls
