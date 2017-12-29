from django.forms import ModelForm, TextInput, NumberInput, EmailInput
from django import forms 
from .models import Profile, Family, BaseModel
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # widgets = {
        #     'first': TextInput(attrs = {
        #         'placeholder': 'dbz name',
        #         'class' : 'blue border'
        #     }),
        #     'last': TextInput(attrs = {
        #         'placeholder': 'saiyan name'
        #     }),
        #     'age': NumberInput( attrs = {
        #         'placeholder': '95' }),
        #     'email': EmailInput( attrs ={'id': 'bg'}),
         
        # }

#Form below not used yet
class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = '__all__'

        widgets = {
            'name' : TextInput( attrs= {
                'placeholder':'choose one'
            })
        }

#Creating Validation Error
def even(value):
    if value % 2 !=0:
        raise ValidationError(
            'Value must be even'
        )


class PForm(forms.Form):
    first = forms.CharField(max_length=15, min_length=9,
     widget=forms.TextInput(attrs={
        'placeholder': 'dbz name',
        'class': 'blue border'
    }))
    last= forms.CharField(max_length = 15, 
    widget = forms.TextInput(attrs={
        'placeholder': 'saiyan name'
    }))
    age= forms.IntegerField(validators = [MaxValueValidator(30), even],
    widget = forms.NumberInput(attrs={
        'placeholder': '95'}))
    email = forms.EmailField( 
        widget = forms.EmailInput( attrs ={'id': 'bg'}))
    telephone = forms.CharField(initial='915', label= 'Label 4 Telephone', widget = forms.TextInput)
    

class ProfileForm2(forms.Form):
    name = forms.CharField(max_length=45, min_length = 5)
    email = forms.EmailField(max_length=45, min_length=5, widget= forms.EmailInput(attrs={'placeholder':'random words'}))
    age = forms.IntegerField(widget= forms.PasswordInput)
