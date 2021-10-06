from django import forms
from django.forms import fields
from .models import Registration
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    """ Registration form """

    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']

    def clean(self):
        data = self.changed_data
        password = data['password']
        conf_password = data['confirm_password']
        
        if password != conf_password:
            raise ValidationError('Confirm password did not match!')

        return super().clean()