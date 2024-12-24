from django import forms
from App_Login.models import CustomUser
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class SignUpForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords do not match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            return user

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            raise ValidationError('Invalid Credentials')

        cleaned_data['user'] = user
        return cleaned_data




