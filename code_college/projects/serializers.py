from rest_framework import serializers
from .models import Project, ProjectImage
from users.serializers import OrdinaryUserSerializer


class ProjectImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectImage
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    project_image = ProjectImageSerializer(many=True, read_only=True)
    owner = OrdinaryUserSerializer()
    contributors = OrdinaryUserSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'owner',
            'contributors',
            'project_image',
            'title',
            'description',
            'repository',
            'deploy',
        ]
