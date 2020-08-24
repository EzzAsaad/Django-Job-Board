from django import forms
from .models import Apply
"""
i made form to let django save each "apply" obj
but i don't need that i can use normal form in html

"""
class ApplyForm(forms.ModelForm):
    
    class Meta:
        model = Apply
        fields = ("name","email","link","cv","coverletter") #Fileds Which will be appear in your form
