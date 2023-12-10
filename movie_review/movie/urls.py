from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('success', views.success, name="success"),
    path('rate/<int:id>', views.rate, name='rate'),
    path('upload/', views.image_upload, name='image-upload')
]