from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Customer

class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email'] # password1 and password2 are included by default
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help text and add Bootstrap classes
        for field in self.fields:
            self.fields[field].help_text = None  # This removes the "Your password must..." text
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter {self.fields[field].label}'
            })

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','mobile_no','city','state','pincode']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'locality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Locality/Street'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pincode'}),
        }