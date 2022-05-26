import imp
from django.contrib import admin
from . models import blog
# Register your models here.

admin.site.register(blog)


# Then ren this command-> python manage.py makemigrations ... to convert this table into code 0001 file 
#Then ren this -> python manage.py migrate .. to save the table inside the db.sqlit file