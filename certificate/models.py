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


class InterviewType(models.Model):
    """
    Тип співбесіди
    """
    title = models.CharField(max_length=40, verbose_name=_('Тип співбесіди'))
    result = models.CharField(max_length=40, verbose_name=_('Результат співбесіди'))
    interview = models.ForeignKey('certificate.Interview', on_delete=models.CASCADE, related_name='interview_types')

    class Meta:
        verbose_name = _('Тип співбесіди')
        verbose_name_plural = _('Типи співбесіди')

    def __str__(self):
        return self.title


class Interview(models.Model):
    """
    Співбесіда
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE)
    start_on = models.DateField(verbose_name=_('Дата співбесіди'), null=True, blank=True)

    class Meta:
        verbose_name = _('Співбесіда')
        verbose_name_plural = _('Співбесіди')

    def __str__(self):
        return self.start_on


class TestType(models.Model):
    """
    Тип тестування
    """
    title = models.CharField(max_length=40, verbose_name=_('Тип тестування'))
    result = models.CharField(max_length=40, verbose_name=_('Результат тестування'))
    interview = models.ForeignKey('certificate.Test', on_delete=models.CASCADE, related_name='test_types')

    class Meta:
        verbose_name = _('Тип тестування')
        verbose_name_plural = _('Типи тестування')

    def __str__(self):
        return self.title


class Test(models.Model):
    """
    Тестування
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE)
    start_on = models.DateField(verbose_name=_('Дата тестування'), null=True, blank=True)

    class Meta:
        verbose_name = _('Тестування')
        verbose_name_plural = _('Тестування')

    def __str__(self):
        return self.start_on


class Training(models.Model):
    """
    Тренування
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE)
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
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE)
    solo = models.BooleanField(_('Вивчив сам'), default=False)
    course = models.BooleanField(_('Прослухав курс'), default=False)

    class Meta:
        verbose_name = _('Польська мова')
        verbose_name_plural = _('Польська мова')

    def __str__(self):
        return self.solo
