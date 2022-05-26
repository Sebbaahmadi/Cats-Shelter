from django.shortcuts import render

# Create your views here.

def for_adoption(request):
    return render(request,'for_adoption/for_adoption.html')


