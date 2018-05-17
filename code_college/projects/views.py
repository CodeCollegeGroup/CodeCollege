from rest_framework import viewsets
from .models import Project, ProjectImage
from .serializers import ProjectSerializer, ProjectImageSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectImageViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectImageSerializer
    queryset = ProjectImage.objects.all()
