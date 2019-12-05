from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
class Volunteer(TemplateView):
    template_name = "volunteers/index.html"


class Signup(TemplateView):
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

        
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    