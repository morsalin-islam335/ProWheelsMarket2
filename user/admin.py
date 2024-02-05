from django.contrib import admin

# Register your models here.
from . models import Buyer, Owner

admin.site.register(Buyer)
admin.site.register(Owner)

