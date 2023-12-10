from django.shortcuts import render
from . import utilities

# Create your views here.
#search by address
def home(request):
    if request.method =='POST':
        address = request.POST.get('address')
        location = utilities.location_by_address(address)
        context = {
            'latitude': location['lat'],
            'longitude': location['lon']
        }
        return render(request, 'home.html',context)
    return render(request, 'home.html')

#search by cordinates
def index(request):
    if request.method =='POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        context = {
            "address": utilities.address_by_location(latitude,longitude)
        }
        return render(request, "index.html", context)
    return render(request, "index.html")

#landing page
def landing(request):
    return render(request, "landing.html")