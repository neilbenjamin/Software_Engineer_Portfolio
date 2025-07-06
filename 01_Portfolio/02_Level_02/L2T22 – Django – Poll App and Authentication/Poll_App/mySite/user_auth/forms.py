from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

# Assistance from codemy.com and Dave GRay YouTube with adding the extra
# field and styling.


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':
                                 'form-control'}), max_length=100)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
