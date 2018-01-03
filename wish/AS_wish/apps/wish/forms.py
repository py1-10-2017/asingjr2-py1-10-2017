from django import forms
from django.forms import TextInput, EmailInput, DateInput
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

def hired(value):
    if value == 'mm/dd/yyyy':
        messages.warning(request, 'confirm password must match password')
        raise ValidationError(
            'confirm password must match password'
        )


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=200, min_length=3,widget=forms.TextInput(), validators = [MinLengthValidator(3, message='username must be at least 3 characters')])
    username = forms.CharField(max_length=200, min_length=3,widget=forms.TextInput(), validators = [MinLengthValidator(3, message='username must be at least 3 characters')])
    password = forms.CharField(
        max_length=200, min_length=3,  widget=forms.PasswordInput())
    confirm_pw = forms.CharField( label='Confirm Password',
        max_length=200, min_length=3,  widget=forms.PasswordInput())

class ItemForm(forms.Form):
    name = forms.CharField(label = 'Item/Product', max_length=200, min_length=4,widget=forms.TextInput())
