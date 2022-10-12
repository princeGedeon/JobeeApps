from django.urls import path
from . import views
urlpatterns = [
    path('jobs/', views.AllJobs.as_view(),name="jobs"),
    path('jobs/<str:pk>', views.getJob, name="get_job"),
path('update/jobs/<str:pk>', views.UpdateJobs.as_view(), name="update_job"),
    path('delete/jobs/<str:pk>', views.DeleteJobs.as_view(), name="delete_job"),
    path('create/jobs',views.CreateJobs.as_view(),name="create_job"),
    path('stats/<str:topic>',views.getTopicStats,name="stats_topic")
]
