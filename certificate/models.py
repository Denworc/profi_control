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
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='certificates')
    welding_type = models.ForeignKey(WeldingType, on_delete=models.CASCADE,
                                     verbose_name=_('Метод зварювання'), related_name='certificates')
    organization = models.CharField(max_length=60, verbose_name=_('Сертифікуюча організація'))
    welding_position = models.CharField(max_length=60, verbose_name=_('Просторове положення'))
    thickness = models.CharField(max_length=60, verbose_name=_('Товщина'))
    certification_date = models.DateField(verbose_name=_('Дата сертифікації'), null=True, blank=True)
    paying_date = models.DateField(verbose_name=_('Дата оплати'), null=True, blank=True)
    start_on = models.DateField(verbose_name=_('Дата видачі'), null=True, blank=True)
    expire = models.DateField(verbose_name=_('Дата завершення'), null=True, blank=True)
    certificate_scan = models.ImageField(verbose_name=_('Скан копія'), blank=True, null=True, upload_to="user/certificates")

    class Meta:
        verbose_name = _('Сертифікат')
        verbose_name_plural = _('Сертифікати')

    def __str__(self):
        return self.welding_type.title


class InterviewType(models.Model):
    """
    Тип співбесіди
    """
    title = models.CharField(max_length=40, verbose_name=_('Тип співбесіди'))

    class Meta:
        verbose_name = _('Тип співбесіди')
        verbose_name_plural = _('Типи співбесіди')

    def __str__(self):
        return self.title


class Interview(models.Model):
    """
    Співбесіда
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='interviews')
    type = models.ForeignKey('certificate.InterviewType', on_delete=models.CASCADE, verbose_name=_('Тип співбесіди'), related_name='interviews')
    result = models.CharField(max_length=40, verbose_name=_('Результат співбесіди'))
    start_on = models.DateField(verbose_name=_('Дата співбесіди'), null=True, blank=True)

    class Meta:
        verbose_name = _('Співбесіда')
        verbose_name_plural = _('Співбесіди')

    def __str__(self):
        return self.result


class TestType(models.Model):
    """
    Тип тестування
    """
    title = models.CharField(max_length=40, verbose_name=_('Тип тестування'))

    class Meta:
        verbose_name = _('Тип тестування')
        verbose_name_plural = _('Типи тестування')

    def __str__(self):
        return self.title


class Test(models.Model):
    """
    Тестування
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='tests')
    type = models.ForeignKey('certificate.TestType', on_delete=models.CASCADE, related_name='tests')
    result = models.CharField(max_length=40, verbose_name=_('Результат тестування'))
    start_on = models.DateField(verbose_name=_('Дата тестування'), null=True, blank=True)

    class Meta:
        verbose_name = _('Тестування')
        verbose_name_plural = _('Тестування')

    def __str__(self):
        return self.result


class Training(models.Model):
    """
    Тренування
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='trainings')
    result = models.CharField(max_length=40, verbose_name=_('Результат тренування'))
    start_on = models.DateField(verbose_name=_('Дата початку тренування'), null=True, blank=True)
    expire = models.DateField(verbose_name=_('Дата завершення тренування'), null=True, blank=True)

    class Meta:
        verbose_name = _('Тренування')
        verbose_name_plural = _('Тренування')

    def __str__(self):
        return self.result


class Polish(models.Model):
    """
    Польська мова
    """
    user = models.OneToOneField('user_profile.User', on_delete=models.CASCADE, related_name='polish')
    solo = models.BooleanField(_('Вивчив сам'), default=False)
    course = models.BooleanField(_('Прослухав курс'), default=False)

    class Meta:
        verbose_name = _('Польська мова')
        verbose_name_plural = _('Польська мова')

    def __str__(self):
        if self.solo:
            return "Вивчив сам"
        elif self.solo:
            return "Прослухав курс"
        else:
            return "Не вивчав"
