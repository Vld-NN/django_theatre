from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def homepage(requests):
    welcome_text = '<h1>Добро пожаловать на сайт нашего театра! </h1>'
    return HttpResponse(welcome_text)
