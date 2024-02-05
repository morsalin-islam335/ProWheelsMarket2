from django.db import models

# Create your models here.

from django.contrib.auth.models import User  


from django.contrib.auth.models import User # user model sob jaygay use korta hoiba jeta authentication er jono use kora hoiba

class Owner(models.Model):
    profile_pic = models.ImageField(upload_to='user/media/uploads/', null = True, blank = True, verbose_name ="Profile Picture", help_text='This is optional') # user chaila tar profile pic dita  para na chaila na
    user = models.OneToOneField(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'applicationUser')
    isOwner = models.BooleanField(default =True, blank = True, null = True, verbose_name = 'Is Owner')
    
    def __str__(self):
        return f"{self.user.username}"





class Buyer(models.Model): #Buyer cahila item buy korta para
    user = models.OneToOneField(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'applicationUser2')
    profile_pic = models.ImageField(upload_to='user/media/uploads/', null = True, blank = True) # user chaila tar profile pic dita  para na chaila na
    isOwner = models.BooleanField(default =False, blank = True, null = True)


    def __str__(self):
        return f'{self.user.username}'