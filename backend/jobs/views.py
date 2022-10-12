
from django.shortcuts import render, get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import generics
from jobs.serializers import JobSerailizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg,Min,Max,Count

from .filters import JobFilter
from .models import Job

# Create your views here.
from .pagination import StandardResultsSetPagination


@api_view(['GET'])
def getAllJobs(request):
    filterset=JobFilter(request.GET,queryset=Job.objects.all().order_by('id'))


    data=JobSerailizer(filterset.qs,many=True).data

    return Response(data)


@api_view(['GET'])
def getJob(request,pk):
    job=get_object_or_404(Job,id=pk)
    serializer=JobSerailizer(job)

    return Response(serializer.data)


@api_view(['GET'])
def getTopicStats(request,topic):
    args={
        'title__icontains':topic
    }
    jobs=Job.objects.filter(**args)
    if len(jobs)==0:
        return Response({"Message":"Not Stats found for {topic}".format(topic=topic)})

    stats=jobs.aggregate(
        total_jobs=Count('title'),
        avg_salaty=Avg('salary'),
        min_salary=Min('salary'),
        max_salart=Max('salary')


    )

    return Response(stats)

#CBV

class DeleteJobs(generics.DestroyAPIView):
    serializer_class = JobSerailizer
    queryset = Job.objects.all()

class CreateJobs(generics.CreateAPIView):
    serializer_class = JobSerailizer
    queryset = Job.objects.all()

class UpdateJobs(generics.UpdateAPIView):
    serializer_class = JobSerailizer
    queryset = Job.objects.all()


class AllJobs(generics.ListAPIView):
    serializer_class = JobSerailizer
    queryset = Job.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = JobFilter
    pagination_class = StandardResultsSetPagination

class UnoJobs(generics.RetrieveAPIView):
    serializer_class = JobSerailizer
    queryset = Job.objects.all()
