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



class CustomUser(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['created_at', 'updated_at']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'is_owner': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
