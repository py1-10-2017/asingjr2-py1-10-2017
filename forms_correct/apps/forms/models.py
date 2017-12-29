# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator, MinValueValidator, MaxValueValidator
from django.forms import ModelForm
# Create your models here.

def even(value):
    if value % 2 != 0:
        raise ValidationError(
            'Age must be even'
        )

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Profile(BaseModel):
    first = models.CharField(max_length=15, unique = True, 
    validators=[
        MinLengthValidator(2, message='Must be at least two characters'),
        MaxLengthValidator(15, message='Must be at least two characters')])
    last = models.CharField(max_length=200)
    age = models.IntegerField(validators = [
        even, MinLengthValidator(21, message='Must be between 21 and 100'), MaxValueValidator(100, message='Must be between 21 and 100')])
    email = models.EmailField(max_length=200, validators = [EmailValidator])
    telephone = models.CharField(max_length=10, default = '915')


    def __unicode__(self):
        return 'first = {} and age = {}'.format(self.first, self.age)

FAMILY_CHOICES = (
    ('Jones', 'JONES'),
    ('Harris', 'HARRIS'),
    ('Sings', 'SINGS'), 
    ('Smiths', 'SMITHS')
)
class Family(BaseModel):
    name = models.CharField(max_length=100, choices = FAMILY_CHOICES)
    members = models.name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __unicode__(self):
        return 'name = {} '.format(self.name)


class Movie(BaseModel):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, 
        validators = [ MinLengthValidator(2, message='value too shoooooooort')]
    )

class MovieForm(ModelForm):
    class Meta:
        model = Movie 
        fields = '__all__'


