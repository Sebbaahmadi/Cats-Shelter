#we use the path..  use the view from the same folder 
from django.urls import path
from . import views


#It's taking request from url, then return response
#it can be a http response which is a message response or render response (html file)
urlpatterns=[
    #first path('the name of the link',views.function,name).. it's consider as an index or home page
    path('',views.blg,name='blog'),
    ]