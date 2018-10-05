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


class QuotaType(models.Model):
    """
    Тип Квоти
    """
    name = models.CharField(max_length=40, verbose_name=_('Тип квоти'))
    title = models.TextField(max_length=400, verbose_name='Опис квоти')

    class Meta:
        verbose_name = _('Тип квоти')
        verbose_name_plural = _('Типи квот')

    def __str__(self):
        return self.title


class Quota(models.Model):
    """
    Квоти
    """
    user = models.ForeignKey(User, verbose_name='Працівник', on_delete=models.CASCADE)
    type = models.ForeignKey(QuotaType, verbose_name=_('Тип квоти'), on_delete=models.CASCADE)
    expire = models.DateField(verbose_name=_('Закінчення квоти'), null=True, blank=True)

    class Meta:
        verbose_name = _('Квоти')
        verbose_name_plural = _('Квоти')

    def __str__(self):
        return self.type.name
