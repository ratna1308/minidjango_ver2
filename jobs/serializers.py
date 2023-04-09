from rest_framework import serializers
from jobs.models import Portal, JobDescription


class PortalSerializer(serializers.Serializer):
    """
    Serializer for `Portal` class
    """

    name = serializers.CharField(required=True, max_length=250)
    description = serializers.CharField(max_length=250)

    def create(self, validated_data):
        return Portal.objects.create(**validated_data)


class JobDescriptionSerializer(serializers.Serializer):
    """
    Serializer for `JobDescription` model class
    """

    role = serializers.CharField(max_length=250)
    description_text = serializers.CharField(max_length=250)
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        return JobDescription.objects.create(**validated_data)


class JobTitleSerializer(serializers.Serializer):
    """
    TODO
    Refer following document nested serializer-
    https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
    """

    title = serializers.CharField(max_length=250)
    last_updated = serializers.DateTimeField(required=True)

    # how to define relationship fields in serializers
    job_description = JobDescriptionSerializer(required=True)
    portal = PortalSerializer(required=True)