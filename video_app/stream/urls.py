from . import views
from . views import (
    VideoDeleteView,
    UserVideoListView,
    VideoCreateView,
    GeneralVideoListView,
    VideoUpdateView,
    VideoDetailView,
) 
from django.urls import path

urlpatterns = [
    path('',GeneralVideoListView.as_view(), name="video-list"),
    path('video-detail/<int:pk>/', VideoDetailView.as_view(), name="video-detail"),
    path('video/<int:pk>/update/', VideoUpdateView.as_view(), name="video-update"),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name="video-delete"),
    path('user/<str:username>', UserVideoListView.as_view(), name="user-videos"),
    path('video/new/',VideoCreateView.as_view(), name="video-create"),
    path('search',views.search,name="search"),
]
