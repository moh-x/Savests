from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .choices import DEPARTMENT_CHOICES, LEVEL_CHOICES


class User(AbstractUser):
    # sv003

    email = models.EmailField(_('email address'), blank=False)
    name = models.CharField(_('real name'), max_length=30, blank=False)
    department = models.CharField(
        max_length=1, choices=DEPARTMENT_CHOICES, default='J')
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default='S')

    REQUIRED_FIELDS = ['email', 'name']

    def get_full_name(self):
        return self.name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        first_name = self.name.split()[0]
        return first_name


class Email(models.Model):
    to = models.ManyToManyField(User, related_name="inbox")
    subject = models.CharField(
        _('Subject'), max_length=100, default='No subject')
    body = models.TextField(_('Body'), default='-------Empty------')
