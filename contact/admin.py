from django.contrib import admin

# Register your models here.
from . models import Contact 

# Register your models here. (we import contact before to use it here)
admin.site.register(Contact)