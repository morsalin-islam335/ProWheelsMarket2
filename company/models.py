from django.db import models

# Create your models here.


from user.models import Owner
class Category(models.Model):
    owner = models.ForeignKey(Owner, on_delete = models.CASCADE, related_name = 'categories',  blank = True, null = True) # ekjon owner ekadhik company er item  add korta parba
    brand = models.CharField(max_length = 100, null = True, blank = True)
    slug = models.SlugField(max_length = 200, blank = True, null = True)

    def __str__(self):
        return f'{self.brand}'

    
