from django  import forms  

from . models import Category
class addBrandForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['brand']
