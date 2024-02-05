from django.contrib import admin

# Register your models here.


from . models import Car 

admin.site.register(Car)

from . models import  Comment
admin.site.register(Comment)