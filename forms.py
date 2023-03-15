from django import forms
from .models import UserSignup,UserSignin


class UsForm(forms.ModelForm):
    class Meta:
        model = UserSignup
        fields = ['username','fname','lname','email','pass1','pass2']

class Uslogin(forms.ModelForm):
    class Meta:
        model = UserSignin

        fields = ['username', 'pass1']