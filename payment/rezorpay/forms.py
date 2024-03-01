from django import forms
from .models import ItemModel

class PaymentForm(forms.ModelForm):
    class Meta:
        model = ItemModel
        fields = ['name','amount']