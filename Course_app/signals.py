# Course_app/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Student

import random

@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'student'):
        Student.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email,
            roll=random.randint(1000, 9999)
        )