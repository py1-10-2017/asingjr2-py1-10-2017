from django import forms
from .models import *

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=45, min_length = 5)
    email = forms.EmailField(max_length=45, min_length=5, widget= forms.EmailInput(attrs={'placeholder':'random words'}))
    age = forms.IntegerField(widget= forms.PasswordInput)

class PlayForm(forms.Form):
    play1 = forms.CharField(label = 'Textarea Widget', widget=forms.Textarea( 
        attrs = {'placeholder':'trying attrs with form'}
        )        )
    play2 = forms.CharField(label= 'Password Widget',widget=forms.PasswordInput)
    play4 = forms.TimeField(label='Time Widget', widget=forms.TimeInput)
    play5 = forms.CharField(label='Checkbox try', widget = forms.CheckboxInput) 

#Creating to gest with Generic Class View
class GenericForm(forms.Form):
    hero = forms.CharField(max_length=6,
    min_length=3,
    label='max is 6 and min is 3',
    widget=forms.TextInput(attrs={ 'placeholder':'overawatch'}))