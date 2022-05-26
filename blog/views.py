import imp
from multiprocessing.spawn import import_main_path
from django.shortcuts import render
from . models import blog

# Create your views here.
def blg(request):
    #create a copy from the blog and save it in post
    post = blog.objects.all()

    #3rd argument -> to send the data to HTML blog
    return render(request,'blog/blog.html',{'post':post})