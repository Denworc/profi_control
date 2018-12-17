from django.db import models
from django.utils.translation import ugettext as _


class Dwelling(models.Model):
    """
    Місце проживання
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='dwellings')
    address = models.CharField(max_length=40, verbose_name='Адреса проживання', blank=True)
    landlord_name = models.CharField(max_length=40, verbose_name="Ім'я орендодавця", blank=True)
    neighbor_name = models.CharField(max_length=40, verbose_name='ПІБ сусіда по кімнаті', blank=True)
    start_on = models.DateField(verbose_name=_('Дата заселення'), null=True, blank=True)
    expire = models.DateField(verbose_name=_('Дата вивільнення'), null=True, blank=True)
    end_date = models.DateField(verbose_name=_('Кінцева дата'), null=True, blank=True)

    class Meta:
        verbose_name = _('Місце проживання')
        verbose_name_plural = _('Місця проживання')

    def __str__(self):
        return self.address
