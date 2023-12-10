from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse

# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def men(request):
    return HttpResponse('meeee jksfkjdfkj xdfkjdfjhk en')

def leg(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

def list(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('list.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context, request))

def daaata(request):
    mdata= {
        'name':'john doe',
        'age':30,
        'email':'johndoe@example.com'
    }
    response = JsonResponse(mdata, status=200)
    return response

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('list'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse("list"))

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('list'))