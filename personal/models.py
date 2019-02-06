from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Email(models.Model):
    email = models.EmailField(default='', help_text='Entrer une adresse email valide <br><br>')

    def save_email(self):
        data = self.cleaned_data['email']
        return data


#@receiver(post_save, sender=User)
def update_email(sender,instance, update, **kwargs):
    if update:
        Email.objects.update(email=instance)
    instance.Email.save()
