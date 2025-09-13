from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['phone_number', 'username','email', 'password1', 'password2']
        
        
        def clean_phone_number(self):
            phone_number = self.cleaned_data.get('phone_number')
            if len(phone_number) != 11:
                raise forms.ValidationError("شماره تلفن باید 11 رقم باشد.")
            return phone_number
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Phone Number",
        widget=forms.TextInput(attrs={"autofocus": True})
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username.isdigit():
            raise forms.ValidationError("لطفا فقط عدد وارد کنید")
        if len(username) != 11:
            raise forms.ValidationError("شماره باید 11 رقم باشد")
        return username


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'profile_pic']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply Bootstrap styles + placeholders
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
        self.fields['profile_pic'].widget.attrs.update({
            'class': 'form-control'
        })

        
        