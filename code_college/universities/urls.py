from rest_framework import routers
from .views import UniversityViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register(r'^university', UniversityViewSet)

urlpatterns = ROUTER.urls
