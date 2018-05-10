from rest_framework import routers
from users.views import OrdinaryUserViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register(r'^ordinary_user', OrdinaryUserViewSet)

urlpatterns = ROUTER.urls
