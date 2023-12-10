from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from . models import VidStream
from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView #help in creaing automatic querys
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  #for verification and authentication
from django.contrib.auth.models import User  # for global user created automatically by django


# Create your views here.
#view for video upload
class VideoCreateView(LoginRequiredMixin, CreateView):
    model = VidStream
    success_url = "/"
    template_name = 'post-video.html'   # this tempalt contains form.as_p variable that automatically creates form interface using the fields below basing on the model
    fields = ['title','description','video']
    
    #this isto make sure that the logged in user is the one to upload the content
    
    def form_invalid(self, form):
        form.instance.streamer = self.request.user
        return super().form_valid(form)
    
 
 #view for listing videos   
class GeneralVideoListView(ListView):
    model  = VidStream
    template_name = 'video-list.html'
    context_object_name = 'videos'
    ordering = ['-upload_date']
    
#video updating
class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = VidStream
    template_name = 'video-update.html'
    success_url="/"
    fields = ['title', 'description','video']
    
    #this is to make sure that user is logged in to upload
    def form_valid(self, form):
        form.instance.streamer = self.request.user
        return super().form_valid(form)
    #this function prevents other people from upadting ypur videos
    def test_func(self):
        video = self.get_object()
        if self.request.user == video.streamer:
            return True
        return False
    
# seeing each individual postin email
class VideoDetailView(DetailView):
    model = VidStream
    template_name = "video-detail.html"
    
 # searching  for video based on title
def search(request):
    if request.method == 'POST':
        query  = request.POST.get('title',None)
        if query:
            results = VidStream.objects.filter(title__contains=query)
            return render(request, 'search.html',{'videos':results})
        else:
            return redirect('search')
    else:
        return render(request, 'search.html')  

# deleting videos
class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "video-confirm-delete.html"
    success_url = "/"
    model = VidStream
    def test_func(self):
        video = self.get_object()
        if self.request.user == video.streamer:
            return True
        return False
    
#query all videos belongingto certain user
class UserVideoListView(ListView):
    model = VidStream
    template_name = "user_videos.html"
    context_object_name = 'videos'
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return VidStream.objects.filter(streamer=user).order_by('-upload')