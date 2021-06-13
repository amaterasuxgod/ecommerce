from django import forms
from django.contrib.auth.forms import (PasswordResetForm, SetPasswordForm)
from .models import UserBase



class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Введите имя пользователя', min_length=4, max_length=50, help_text='Обязательно')
    email = forms.EmailField(max_length=100, help_text='Обязательно', error_messages={'required': 'Простите, требуется ввести email'})
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email', )               

    
    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Такой пользователь уже существует")
        return user_name
    
    def check_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Пароли не совпадают")
        return data['password2']
    
    def email_check(self):
        email = self.cleaned_data['email']
        email = UserBase.objects.filter(email=email)
        if email.count():
            raise forms.ValidationError('Данный email уже привязан к аккаунту')
        return email

class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Данный email не привязан ни к какому аккаунту')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'placeholder': 'New Password', 'id': 'form-new-pass2'}))


class UserEditForm(forms.ModelForm):

    email = forms.CharField(widget=forms.TextInput(
            attrs={'readonly': 'readonly'}))
    
    phone_number = forms.CharField(min_length=4, max_length=50)

    postcode = forms.CharField()

    address_line_1 = forms.CharField()

    town_city = forms.CharField()

    class Meta:
        model = UserBase
        fields = ('email', 'phone_number', 'postcode', 'address_line_1', 'town_city',)
    

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)


    
