from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _


class ExtendUser(AbstractUser):
    username = models.CharField(unique=True, max_length=150, null=True, blank=True)
    email = models.EmailField(verbose_name="email address", max_length=150, unique=True)
    reset_password_token = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.id) + self.email
