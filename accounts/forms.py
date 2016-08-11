from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class RegistrationForm(UserCreationForm):
    quiz_answer = forms.CharField()

class MyAuthenticationForm(AuthenticationForm):
    quiz_answer = forms.CharField()
