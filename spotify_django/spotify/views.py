from django.shortcuts import render, redirect, get_object_or_404
from . forms import UserRegistrationForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from . models import SpotMusic
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form  = UserRegistrationForm(request.POST)
        #username = request.POST['username']
        #print(username)
        #password1 = request.POST['password1']
        #print(password1)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('signup')
    else:
        form = UserRegistrationForm()
        return render (request,'register.html',{'form':form})

"""   
when using LoginForm
def login(request):
    if request.method =='PSOT':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                form = LoginForm()
                return render(request,'login.html',{'from':form})
        else:
            form = LoginForm()
            return render(request,'login.html',{'form':form})
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})
        
"""

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #print(password)
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('login')



#classbased view for uploading audio
class SongCreateView(LoginRequiredMixin, CreateView):
    model = SpotMusic
    template_name = 'song-create.html'
    fields = ['song_author','song_title','song_image','audio']
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
    
#displaying all songs
@login_required(login_url='login')
def home(request):
    songs = SpotMusic.objects.all()
    return render(request, 'home.html',{'all':songs})

def playSong(request, id):
    song = SpotMusic.objects.get(id=id)
    return render(request, 'playsong.html',{'song':song})