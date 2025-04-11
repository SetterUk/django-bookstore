# store/forms.py
from django import forms
from .models import CartItem

class CartAddBookForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 80px'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)