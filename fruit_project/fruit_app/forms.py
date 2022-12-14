from django import forms
from .models import fruit_shop
class FruitForm(forms.ModelForm):
    class Meta:
        model=fruit_shop
        fields=['name','desc','price','image']