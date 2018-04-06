from rest_framework import viewsets
from .models  import OrdinaryUser
from .serializers import OrdinaryUserSerializer

class OrdinaryUserViewSet(viewsets.ModelViewSet):

    serializer_class = OrdinaryUserSerializer
    queryset = OrdinaryUser.objects.all()
