from rest_framework import viewsets
from .models import University
from .serializers import UniversitySerializer


class UniversityViewSet(viewsets.ModelViewSet):

    serializer_class = UniversitySerializer
    queryset = University.objects.all()
