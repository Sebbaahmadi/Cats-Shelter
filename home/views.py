from statistics import harmonic_mean 
from django.shortcuts import render
from django.http import  HttpResponse

# View page in the middel to linke the backend , frontend and DB
# Create your views here.

# def hi(requset):
#     return HttpResponse('Hi')

def hi(request):
    return render(request,'home/home.html')

#the view taking the requst url, and view will return render response which is the html file 'where to find the html file'  
def about(request):
    return render(request,'home/about.html')


