from django.urls import path
from . import views
urlpatterns = [

    path('signup/',views.register,name="signup"),
    path('me/',views.currentUser,name="me"),

]