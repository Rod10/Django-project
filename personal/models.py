from django.db import models


class Email(models.Model):
    email = models.EmailField(default='', help_text='Entrer une adresse email valide <br><br>')

    def save_email(self):
        data = self.cleaned_data['email']
        return data


def update_email(sender,instance, update, **kwargs):
    if update:
        Email.objects.update(email=instance)
    instance.Email.save()
