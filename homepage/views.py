from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.views.generic import TemplateView

from plays.models import Show


# Create your views here.
#def homepage(requests):
    #return TemplateResponse(requests,'homepage.html')

class HomepageView(TemplateView):
    template_name = 'homepage.html'
    model = Show


