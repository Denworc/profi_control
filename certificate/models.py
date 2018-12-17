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
                                     verbose_name=_('Метод зварювання'), related_name='certificates', null=True, blank=True)
    organization = models.CharField(max_length=60, verbose_name=_('Сертифікуюча організація'), blank=True)
    welding_position = models.CharField(max_length=60, verbose_name=_('Просторове положення'), blank=True)
    thickness = models.CharField(max_length=60, verbose_name=_('Товщина'), blank=True)
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
    type = models.ForeignKey('certificate.InterviewType', on_delete=models.CASCADE,
                             verbose_name=_('Тип співбесіди'), related_name='interviews'
                             , null=True, blank=True)
    result = models.CharField(max_length=40, verbose_name=_('Результат співбесіди'), blank=True)
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
    type = models.ForeignKey('certificate.TestType', on_delete=models.CASCADE,
                             related_name='tests', verbose_name=_('Тип тестування'),
                             null=True, blank=True)
    result = models.CharField(max_length=40, verbose_name=_('Результат тестування'), blank=True)
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
    result = models.CharField(max_length=40, verbose_name=_('Результат тренування'), blank=True)
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
        elif self.course:
            return "Прослухав курс"
        else:
            return "Не вивчав"


class DrawReading(models.Model):
    """
    Читання креслень
    """
    title = models.CharField(max_length=40, verbose_name=_('Читання креслень'))

    class Meta:
        verbose_name = _('Читання креслень')
        verbose_name_plural = _('Читання креслень')

    def __str__(self):
        return self.title


class Candle(models.Model):
    """
    Вміння працювати з газовим паяльником
    """
    title = models.CharField(max_length=40, verbose_name=_('Вміння працювати з газовим паяльником'))

    class Meta:
        verbose_name = _('Вміння працювати з газовим паяльником')
        verbose_name_plural = _('Вміння працювати з газовим паяльником')

    def __str__(self):
        return self.title


class Bulgarian(models.Model):
    """
    Вміння працювати болгаркою
    """
    title = models.CharField(max_length=40, verbose_name=_('Вміння працювати болгаркою'))

    class Meta:
        verbose_name = _('Вміння працювати болгаркою')
        verbose_name_plural = _('Вміння працювати болгаркою')

    def __str__(self):
        return self.title


class SemiAutomatic(models.Model):
    """
    Досвід зварювання напівавтоматом
    """
    title = models.CharField(max_length=40, verbose_name=_('Досвід зварювання напівавтоматом'))

    class Meta:
        verbose_name = _('Досвід зварювання напівавтоматом')
        verbose_name_plural = _('Досвід зварювання напівавтоматом')

    def __str__(self):
        return self.title


class WeldMethod(models.Model):
    """
    Спосіб зварювання
    """
    title = models.CharField(max_length=40, verbose_name=_('Спосіб зварювання'))

    class Meta:
        verbose_name = _('Спосіб зварювання')
        verbose_name_plural = _('Способи зварювання')

    def __str__(self):
        return self.title


class MetalBrand(models.Model):
    """
    Марка металу
    """
    title = models.CharField(max_length=40, verbose_name=_('Марка металу'))

    class Meta:
        verbose_name = _('Марка металу')
        verbose_name_plural = _('Марки металу')

    def __str__(self):
        return self.title


class ConnectionType(models.Model):
    """
    Тип з'єднання
    """
    title = models.CharField(max_length=40, verbose_name=_("Тип з'єднання"))

    class Meta:
        verbose_name = _("Тип з'єднання")
        verbose_name_plural = _("Типи з'єднання")

    def __str__(self):
        return self.title


class SpatialPosture(models.Model):
    """
    Просторове положення
    """
    title = models.CharField(max_length=40, verbose_name=_('Просторове положення'))

    class Meta:
        verbose_name = _('Просторове положення')
        verbose_name_plural = _('Просторові положення')

    def __str__(self):
        return self.title


class Other(models.Model):
    """
    Для кандидатів інших спеціальностей
    """
    title = models.CharField(max_length=40, verbose_name=_('Рівень кваліфікації'))

    class Meta:
        verbose_name = _('Рівень кваліфікації')
        verbose_name_plural = _('Рівні кваліфікації')

    def __str__(self):
        return self.title


class QualificationLevel(models.Model):
    """
    Оцінка кваліфікації користувача
    """
    user = models.OneToOneField('user_profile.User', on_delete=models.CASCADE, related_name='qualifications')
    specialization = models.CharField(max_length=300, verbose_name=_('Спеціалізація'), blank=True)
    draw_reading = models.ForeignKey(DrawReading, on_delete=models.CASCADE,
                                     null=True, blank=True, verbose_name=_('Читання креслень'))
    candle = models.ForeignKey(Candle, on_delete=models.CASCADE,
                               null=True, blank=True, verbose_name=_('Вміння працювати з газовим паяльником'))
    bulgarian = models.ForeignKey(Bulgarian, on_delete=models.CASCADE,
                                  null=True, blank=True, verbose_name=_('Вміння працювати болгаркою'))
    semiautomatic = models.ForeignKey(SemiAutomatic, on_delete=models.CASCADE,
                                      null=True, blank=True, verbose_name=_('Досвід зварювання напівавтоматом'))
    welding_method = models.ForeignKey(WeldMethod, on_delete=models.CASCADE,
                                       null=True, blank=True, verbose_name=_('Спосіб зварювання'))
    metal_brand = models.ForeignKey(MetalBrand, on_delete=models.CASCADE,
                                    null=True, blank=True, verbose_name=_('Марка металу'))
    connection_type = models.ForeignKey(ConnectionType, on_delete=models.CASCADE,
                                        null=True, blank=True, verbose_name=_("Тип з'єднання"))
    spatial_posture = models.ForeignKey(SpatialPosture, on_delete=models.CASCADE,
                                        null=True, blank=True, verbose_name=_('Просторове положення'))
    other = models.ForeignKey(Other, on_delete=models.CASCADE,
                              null=True, blank=True, verbose_name=_('Рівень кваліфікації'))
    thickness = models.CharField(max_length=300, verbose_name=_('Товщина'), blank=True)

    class Meta:
        verbose_name = _('Оцінка кваліфікації')
        verbose_name_plural = _('Оцінки кваліфікації')

    # def __str__(self):
    #     return self.contact


class PostQualificationLevel(models.Model):
    """
    Попередня оцінка кваліфікації користувача
    """
    user = models.OneToOneField('user_profile.User', on_delete=models.CASCADE, related_name='post_qualifications')
    specialization = models.CharField(max_length=300, verbose_name=_('Спеціалізація'), blank=True)
    draw_reading = models.ForeignKey(DrawReading, on_delete=models.CASCADE,
                                     null=True, blank=True, verbose_name=_('Читання креслень'))
    candle = models.ForeignKey(Candle, on_delete=models.CASCADE,
                               null=True, blank=True, verbose_name=_('Вміння працювати з газовим паяльником'))
    bulgarian = models.ForeignKey(Bulgarian, on_delete=models.CASCADE,
                                  null=True, blank=True, verbose_name=_('Вміння працювати болгаркою'))
    semiautomatic = models.ForeignKey(SemiAutomatic, on_delete=models.CASCADE,
                                      null=True, blank=True, verbose_name=_('Досвід зварювання напівавтоматом'))
    welding_method = models.ForeignKey(WeldMethod, on_delete=models.CASCADE,
                                       null=True, blank=True, verbose_name=_('Спосіб зварювання'))
    metal_brand = models.ForeignKey(MetalBrand, on_delete=models.CASCADE,
                                    null=True, blank=True, verbose_name=_('Марка металу'))
    connection_type = models.ForeignKey(ConnectionType, on_delete=models.CASCADE,
                                        null=True, blank=True, verbose_name=_("Тип з'єднання"))
    spatial_posture = models.ForeignKey(SpatialPosture, on_delete=models.CASCADE,
                                        null=True, blank=True, verbose_name=_('Просторове положення'))
    other = models.ForeignKey(Other, on_delete=models.CASCADE,
                              null=True, blank=True, verbose_name=_('Рівень кваліфікації'))
    thickness = models.CharField(max_length=300, verbose_name=_('Товщина'), blank=True)

    class Meta:
        verbose_name = _('Попередня оцінка кваліфікації')
        verbose_name_plural = _('Попередня оцінки кваліфікації')

    # def __str__(self):
    #     return self.contact
