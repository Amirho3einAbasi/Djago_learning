from django import forms
from django.contrib.auth import get_user_model

user = get_user_model()


class form_login(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    def clean(self):
        pass1 =  self.cleaned_data.get('password')
        pass2 =  self.cleaned_data.get('password_confirm')
        if pass1 != pass2:
            raise forms.ValidationError('passwords must be the same')
class form_register(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))
    password_confirm = forms.CharField(label='password confirm', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your password again'}))

    def clean(self):
        userName = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_confirm')
        email = self.cleaned_data.get('email')
        qs_username = user.objects.filter(username=userName)
        qs_email = user.objects.filter(email=email)
        if qs_username.exists():
            raise forms.ValidationError('username is taken')
        elif qs_email.exists():
            raise forms.ValidationError('email is taken')
        elif password != password2:
            raise forms.ValidationError('password has be correct')
        else:
            return self.cleaned_data