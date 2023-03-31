from django.shortcuts import render, redirect
from django.http import JsonResponse

from bs4 import BeautifulSoup

import requests

def shiny(request):
    return render(request, 'djangoapp/shiny.html')

def shiny_contents(request):
    response = requests.get('http://127.0.0.1:3737')
    soup = BeautifulSoup(response.content, 'html.parser')
    return JsonResponse({'html_contents': str(soup)})

