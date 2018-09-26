from django import forms
from .models import Users


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30, help_text='Provide a unique user name')
    email = forms.CharField(max_length=30)
    address = forms.CharField(max_length=60)
    birthday = forms.DateField()

    class Meta:
        model = Users
        fields = ('email', 'username', 'address', 'birthday')

