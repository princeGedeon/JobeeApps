from rest_framework import serializers

from jobs.models import Job


class JobSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'
