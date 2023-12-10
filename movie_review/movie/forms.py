from . models import Review
from django import forms
from . views import Movie

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["author", "stars","comment"]
        
class FileuploadForm(forms.ModelForm):
    #title=forms.CharField(max_length=200)
    #description = forms.TimeField()
    #movie_cover = forms.ImageField()
    class Meta:
        model = Movie
        
        fields = ['title','description', 'movie_cover']
        
        
        