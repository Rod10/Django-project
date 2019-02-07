from django import forms
from models import Email


class EmailForm(forms.ModelForm):
    email = forms.EmailField(help_text='Entrer une adresse valide  <br><br> ')

    class Meta:
        model = Email
        fields = ('email',)
        exclude = ('username', 'birth_date', 'password1', 'password2',)
