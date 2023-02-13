import uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(
        verbose_name=_("Username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(
        verbose_name=_("First name"), max_length=50, blank=True
    )
    last_name = models.CharField(verbose_name=_("Last name"), max_length=50, blank=True)
    email = models.EmailField(verbose_name=_("Email address"), unique=True)
    is_staff = models.BooleanField(
        _("Staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("Date joined"), default=timezone.now)
    last_login = models.DateTimeField(_("Last login"), blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def natural_key(self):
        return (self.username,)
