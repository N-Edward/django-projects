from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('men/', views.men, name='men'),
    path('leg/', views.leg, name='leg'),
    path('list/', views.list, name = 'list'),
    path('list/add/', views.add, name='add'),
    path('list/add/addrecord/', views.addrecord, name='addrecord'),
    path('list/update/<int:id>', views.update, name="update"),
    path('list/update/updaterecord/<int:id>', views.updaterecord, name="updaterecord"),
    path('list/delete/<int:id>',views.delete, name="delete"),
    path('daaata/', views.daaata, name='daaata'),
     
]
