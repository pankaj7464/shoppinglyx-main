from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation


class CustomerResistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(
            attrs={'class': 'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_('password'), strip=False, widget=forms.PasswordInput(
        attrs={'autofocus': True, 'class': 'form-control'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old password'), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'current-password', 'autofocus': True}))
    new_password1 = forms.CharField(label=_('New password'), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'new-password', 'autofocus': True}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New password'), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'new-password', 'autofocus': True}))
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_('email'), widget=forms.EmailInput(
        attrs={'class':'form-control', 'autocomplete': 'email', 'autofocus': True}))
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New password'), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'new-password', 'autofocus': True}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New password'), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'new-password', 'autofocus': True}))
