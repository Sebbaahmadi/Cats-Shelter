from django.shortcuts import render
from django.http import  HttpResponse
#from the models import the class because we will create an obj
from .models import Contact 
from django.shortcuts import render



# Create your views here.
def contact(request):
    #it the request that made by the user was post, then colect ahh the below data.. 
    if request.method=='POST':
        #1:gat the data from the form by requsting these data 
        vname=request.POST.get('name') #the name of the input in the contact file 
        vemail=request.POST.get('email')
        vsubject=request.POST.get('subject')
        vmessage=request.POST.get('message')
        #2:send data back to DB to our models, it's an object from this class 
        vcontact= Contact(name=vname, email=vemail, subject=vsubject, message=vmessage)
        #3: save the object back to the DB
        vcontact.save()
        return render(request,'contact/contact.html')
    else:
        return render(request,'contact/contact.html')