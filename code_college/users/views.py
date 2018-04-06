from rest_framework import viewsets
from . import models.OrdinaryUser

class OrdinaryUserViewSet(viewsets.ModelViewSet):

    serializer_class = OrdinaryUserSerializer
    queryset = OrdinaryUser.objects.all()
