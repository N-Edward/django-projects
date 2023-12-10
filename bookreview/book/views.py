from django.shortcuts import render, redirect
from .models import Book, Review
from . forms import ReviewForm

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request,'home.html',{'books':books})

def rev(request, id):
    obj = Book.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        user = request.POST['user']
        stars = request.POST['stars']
        comment = request.POST['comment']
        review = Review(user=user,stars=stars,comment=comment,book=obj)
        review.save()
        return redirect('success')
    else:
        form =ReviewForm()
        context = {
            'form':form,
            'books': obj
        }
        return render(request, 'rev.html', context)
    
def success(request):
    return render(request,'success.hmtl')