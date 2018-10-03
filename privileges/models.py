from django.db import models
from django.utils.translation import ugettext as _
from user_profile.models import User

# Create your models here.


class PrivilegesType(models.Model):
    """
    Тип пільг
    """
    title = models.CharField(max_length=40, verbose_name='Тип пільг')
    user = models.ManyToManyField(User, verbose_name='Працівник')

    class Meta:
        verbose_name = _('Тип пільг')
        verbose_name_plural = _('Типы пільг')

    def __str__(self):
        return self.title


