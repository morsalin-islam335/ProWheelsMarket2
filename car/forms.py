from django import forms

from .models import Car


class addCar(forms.ModelForm):
    class Meta:
        model = Car 
        exclude = ['buyer','owner']
        

from .models import Comment
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['name','car']

      