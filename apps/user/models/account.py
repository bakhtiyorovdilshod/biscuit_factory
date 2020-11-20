from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Account(models.Model):
    gender = [
        ('male', 'male'),
        ('female', 'female')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(
        max_length=6, choices=gender, default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

