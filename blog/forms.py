from django import forms
from blog.models import User

class RegistrationForm(forms.Form):
    model = User
    
    name = forms.CharField(max_length=40,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'First name',
                               'id': 'inputName'
                           }
                        )
                    )
    
    last_name = forms.CharField(max_length=40,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Second name',
                               'id': 'inputLastName'
                           }
                        )
                    )
    
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Email address',
                                 'id': 'inputEmail'
                             }
                        )
                    )

    password = forms.CharField(max_length=40,
                                widget=forms.PasswordInput(attrs={
                                    'class' : 'form-control',
                                    'placeholder' : 'Password',
                                    'id' : 'inputPassword'
                                }
                            )
                        )
    
    password2 = forms.CharField(max_length=40,
                                widget=forms.PasswordInput(attrs={
                                    'class' : 'form-control',
                                    'placeholder' : 'Password confirmation',
                                    'id': 'inputPassword2'
                                }
                            ),
                                help_text=("Enter the same password as above, for verification."))
    
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    
    class Meta:
        model = User
        fields = (
            'name',
            'last_name',
            'email',
            'password'
        )
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
            )
        return password2
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password = self.cleaned_data["password1"]
        user.name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user
