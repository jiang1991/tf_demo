
from django import forms


class LoginForm(forms.Form):
    password = forms.CharField(label='Password', min_length=4, required=True,)
