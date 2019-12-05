from django.urls import path
from .views.volunteer import index
urlpatterns = [
    path('',index)
]
