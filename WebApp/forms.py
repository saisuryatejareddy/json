from .models import Json
from django import forms
class StdForm(forms.ModelForm):
    class Meta :
        model = Json
        fields =[
            'JsonFile',
        ]