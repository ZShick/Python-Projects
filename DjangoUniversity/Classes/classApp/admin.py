from django.contrib import admin

from .models import djangoClasses
#this is importing the class I created from the .models page and letting admins create new instances of the class

admin.site.register(djangoClasses)