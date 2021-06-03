from django.shortcuts import render
from django.http import JsonResponse
import requests
import logging
# Create your views here.

def index(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    log = logging.getLogger("my-logger")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;"}
    r = requests.get(f'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}', headers=headers)
    print(r.content)
    return JsonResponse(r.json())