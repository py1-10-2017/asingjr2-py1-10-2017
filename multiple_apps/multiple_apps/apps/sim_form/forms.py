from django import forms

class Name_Form(forms.Form):
    name = forms.CharField(label='Your Name:', max_length=200, initial='Arthur Initial')
    #Initial works like placeholder but is a real value that will get sent to db if not updated
    #Can be used if you are creating an empty field with a standard value
 