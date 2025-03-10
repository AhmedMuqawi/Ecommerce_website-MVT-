from django import forms
from .models import Cart
from django.core.exceptions import ValidationError

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('quantity',)
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')

        if quantity < 1:
            raise ValidationError("Quantity can not be at least 1")

        return quantity
