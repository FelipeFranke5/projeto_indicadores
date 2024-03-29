from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def criar_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

    for usuario in User.objects.all():
        Token.objects.get_or_create(user=usuario)
