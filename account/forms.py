from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    model = User
    
    username = forms.CharField(max_length=40,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Username',
                           }
                        )
                    )
    
    first_name = forms.CharField(max_length=40,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'First name',
                           }
                        )
                    )
    
    last_name = forms.CharField(max_length=40,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Second name',
                           }
                        )
                    )
    
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Email address',
                             }
                        )
                    )

    password1 = forms.CharField(max_length=40,
                                widget=forms.PasswordInput(attrs={
                                    'class' : 'form-control',
                                    'placeholder' : 'Password',
                                }
                            )
                        )
    
    password2 = forms.CharField(max_length=40,
                                widget=forms.PasswordInput(attrs={
                                    'class' : 'form-control',
                                    'placeholder' : 'Password confirmation',
                                }
                            ),help_text=_("Enter the same password as before, for verification."),
                        )

    
    
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=40,
            widget=forms.TextInput(attrs={
                'autofocus': True,
                'class': 'form-control',
                'placeholder': 'Username',
            }
        ),
    )
    password = forms.CharField(strip=False,
            widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        ),
    )