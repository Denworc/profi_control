from django.db import models
from django.utils.translation import ugettext as _


class WeldingType(models.Model):
    """
    Метод зварювання
    """
    title = models.CharField(max_length=40)

    class Meta:
        verbose_name = _('Метод зварювання')
        verbose_name_plural = _('Методи зварювання')

    def __str__(self):
        return self.title


class Certificate(models.Model):
    """
    Сертифікат
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE)
    welding_type = models.ForeignKey(WeldingType, on_delete=models.CASCADE, verbose_name=_('Метод зварювання'))
    organization = models.CharField(max_length=60, verbose_name=_('Сертифікуюча організація'))
    welding_position = models.CharField(max_length=60, verbose_name=_('Просторове положення'))
    thickness = models.CharField(max_length=60, verbose_name=_('Товщина'))
    start_on = models.DateField(verbose_name=_('Дата видачі'), null=True, blank=True)
    expire = models.DateField(verbose_name=_('Дата завершення'), null=True, blank=True)

    class Meta:
        verbose_name = _('Сертифікат')
        verbose_name_plural = _('Сертифікати')

    def __str__(self):
        return self.welding_type.title
