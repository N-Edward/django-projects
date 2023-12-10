from rest_framework import serializers
from . models import Tutorial

class TutorialSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model  = Tutorial
        fields = ('id','title','description','published')