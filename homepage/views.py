from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.views.generic import ListView

from plays.models import Show


# Create your views here.
#def homepage(requests):
    #return TemplateResponse(requests,'homepage.html')

class HomepageView(ListView):
    template_name = 'homepage.html'
    model = Show

    def get_queryset(self):
        return Show.objects.active()



