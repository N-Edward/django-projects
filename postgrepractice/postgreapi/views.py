from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import JsonResponse

from . models import Tutorial
from . serializer import TutorialSeriaLizer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST','DELETE'])
def tutorial_list(request):
    #retrieve tutorials with condition
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__contains=title)
            tutorials_serializer = TutorialSeriaLizer(tutorials, many = True)
            return JsonResponse(tutorials_serializer.data, safe=False)
            
        else:
            tutorials_serializer = TutorialSeriaLizer(tutorials, many = True)
            return JsonResponse(tutorials_serializer.data, safe=False)
        
    #posting tutorials
    elif request.method =='POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSeriaLizer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorials_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT) 
        
        
@api_view(['GET','PUT','DELETE'])
#single tutorial with id:
def tutorial_detail(request, pk):
    tutorial = Tutorial.objects.get(pk = pk)
    if request.method == 'GET':
        tutorial_serializer = TutorialSeriaLizer(tutorial)
        return JsonResponse(tutorial_serializer.data)
    # upload by id request
    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSeriaLizer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        else:
            return JsonResponse(tutorial_serializer.data)
        
    elif request.method == 'DELETE':
        tutorial.delete
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
        
        
    
    

#getting published
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)
    if request.method == 'GET':
        tutorial_serializer = TutorialSeriaLizer(tutorials, many=True)
        return JsonResponse(tutorial_serializer.data,safe=False)