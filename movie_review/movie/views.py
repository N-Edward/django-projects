from django.shortcuts import render, redirect
from . models import Movie, Review
from . forms import ReviewForm, FileuploadForm
# Create your views here.

def home(request):
    items = Movie.objects.all()
    context = {
        'items':items
    }
    return render (request, 'home.html',context)

def rate(request,id):
    post  = Movie.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        author = request.POST.get('author')
        stars = request.POST.get('stars')
        comment = request.POST.get('comment')
        # inserting into review model/table
        review = Review(author=author, stars = stars, comment = comment, movie=post)
        review.save()
        return redirect('success')
    else:
        form = ReviewForm()
        context = {
            "form":form
        }
        return render(request,'rate.html',context)
    
def success(request):
    return render(request,'success.html')

def image_upload(request):
    if request.method == 'POST':
        # for file uploads always include enctype=multipart/form-data in html form
        # always include request.Files get form data
        form = FileuploadForm(request.POST, request.FILES)
        if form.is_valid():
            movie = Movie()
            movie.title = form.cleaned_data['title']
            movie.description = form.cleaned_data['description']
            movie.movie_cover = form.cleaned_data['movie_cover']
            movie.save()
            return redirect('home')
        else:
            form = FileuploadForm()
            return render(request, 'upload.html',{'form':form})
    else:
        form = FileuploadForm()
        return render(request, 'upload.html',{'form':form})