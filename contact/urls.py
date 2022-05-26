from django.urls import path
from . import views

urlpatterns=[
    #name-> name of url ,, this name will be used inside HTML when we want to mention this pat(inside the actions)
    path('',views.contact,name='contact'),
]