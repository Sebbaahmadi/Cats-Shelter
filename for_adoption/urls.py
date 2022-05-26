#we use the path..  use the view from the same folder 
from django.urls import path
from . import views

urlpatterns=[
    path('',views.for_adoption,name='for_adoption'),
]
