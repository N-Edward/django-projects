from django.urls import path, include
from . import views
from . views import SongCreateView

urlpatterns = [
    path('',views.home, name='home'),
    path('play/<int:id>',views.playSong, name="play"),
    path('create',SongCreateView.as_view(), name='create'),
    
    path('signup',views.signup,name='signup'),
    path('login', views.user_login,name="login"),
    path('logout', views.logout, name='logout')
]