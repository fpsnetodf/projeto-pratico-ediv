from django import forms 
from django.contrib.auth import forms 
from .models import Users



class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users


class RegisterForm(UserCreationForm):
    '''Formulario para cadastro de usuarios sem permissoes administrativa '''   

    class Meta(UserCreationForm.Meta):
        fields = ["first_name", "email"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if 'password' in field:
                self.fields[field].help_text = None
            self.fields[field].widget.attrs.update({'class': "form-control"})
    