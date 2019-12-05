from django.urls import path
from .views.volunteer import Volunteer
urlpatterns = [
    path('',Volunteer.as_view())
]
