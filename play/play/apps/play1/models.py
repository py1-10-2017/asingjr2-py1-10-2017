# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError 
from django.core.validators import EmailValidator, MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
from django.forms import ModelForm


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Profile(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(validators=[EmailValidator(message='Brolly\'s email is stronger'), MinLengthValidator(6, message='Need more characters my friend')])
    age = models.IntegerField(validators=[MaxValueValidator(75,message='Cannot be older than 75'), MinValueValidator(21, message='Must be at least 21')])

    def __unicode__(self):
        return 'name is {}, age is {}'.format(self.name, self.age)

#BELOW IS A TUPLE OF TUPLES.....seperated by commas as a list for data showing in form and on adminside which will be all capital
COLORS = (
    ('red', 'RED'),
    ('blue','BLUE') ,
    ('brown', 'BROWN'),
    ('yellow', 'YELLOW') ,
    ('orange', 'ORANGE')
)

class Color(BaseModel):
    name = models.TextField(validators=[MaxLengthValidator(15, message='Cannot be longer than 15 characters')])
    family = models.CharField(max_length=10, choices = COLORS, default='random')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return 'name is {}, family is {}'.format(self.name, self.family)


#***************************************************************************************
#If you choose to use MODEL FORM foreign key and many to many must be choices from query set!!!
#***************************************************************************************
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        
class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
