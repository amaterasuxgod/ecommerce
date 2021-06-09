from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    name = forms.CharField(label='Введите имя', required=True)
    phone = forms.CharField(label='Введите номер телефона',required=True)
    adress1 = forms.CharField(label='Введите адрес',required=True)
    city = forms.CharField(label='Введите город/населенный пункт',required=True)

    class Meta:
        model = Order
        fields = ('name', 'phone', )    