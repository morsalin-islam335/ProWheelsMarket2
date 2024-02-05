from django import forms 


from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm, SetPasswordForm



from . models import Buyer, Owner

from django.contrib.auth.models import User 

class SignUpFormAsBuyer1(UserCreationForm):
    # first_name = forms.CharField(max_length = 60)
    # last_name = forms.CharField(max_length=60, required= False)

    class Meta:
        model = User
        fields = ["first_name", 'last_name','username','email']


class SignUpAsBuyer2(forms.ModelForm):
    class Meta:
        model = Buyer 
        exclude= ['user','isOwner']



class SignUpAsOwner1(UserCreationForm):
    first_name = forms.CharField(max_length = 60)
    last_name = forms.CharField(max_length=60, required= False)
    class Meta:
        model = User
        fields = ["first_name", 'last_name', 'username','email']
        

        
class SignUpFormAsOwner2(forms.ModelForm):
   
    class Meta:
        model = Owner  
        fields = ['profile_pic']



        