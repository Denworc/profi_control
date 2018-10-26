from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.


class Dismissal(models.Model):
    """
    Звільнення
    """
    user = models.OneToOneField('user_profile.User', on_delete=models.CASCADE, related_name='dismissals')
    dismissal_date = models.DateField(verbose_name=_('Дата звільнення'), null=True, blank=True)
    order_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
    order_number = models.CharField(max_length=40, verbose_name='№ наказу')
    dismissal_reason = models.CharField(max_length=40, verbose_name='Причина звільнення')
    dismissal_basis = models.CharField(max_length=40, verbose_name='Підстава звільнення')

    class Meta:
        verbose_name = _('Звільнення')
        verbose_name_plural = _('Звільнення')

    def __str__(self):
        return self.order_number


class Assignment(models.Model):
    """
    Відрядження
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='assignments')
    order_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
    order_number = models.CharField(max_length=40, verbose_name='№ наказу')
    factory = models.CharField(max_length=40, verbose_name='Завод')
    city = models.CharField(max_length=40, verbose_name='Місто відрядження')
    start_on = models.DateField(verbose_name=_('Початок відрядження'), null=True, blank=True)
    expire = models.DateField(verbose_name=_('Закінчення відрядження'), null=True, blank=True)
    polish_border = models.DateField(verbose_name=_('Перетин кордону в Польщу'), null=True, blank=True)
    ukrainian_border = models.DateField(verbose_name=_('Перетин кордону в Україну'), null=True, blank=True)
    dismissal_reason = models.CharField(max_length=400, verbose_name='Дострокове закінчення')
    dismissal_basis = models.CharField(max_length=400, verbose_name='Переривання відрядження')

    class Meta:
        verbose_name = _('Відрядження')
        verbose_name_plural = _('Відрядження')

    def __str__(self):
        return self.order_number


class AdoptionInState(models.Model):
    """
    Прийняття в штат
    """
    user = models.OneToOneField('user_profile.User', on_delete=models.CASCADE, related_name='adoptions')
    dismissal_date = models.DateField(verbose_name=_('Дата прийняття'))
    order_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
    order_number = models.CharField(max_length=20, verbose_name='№ наказу')

    class Meta:
        verbose_name = _('Прийняття в штат')
        verbose_name_plural = _('Прийняття в штат')

    def __str__(self):
        return self.order_number


class TransferInState(models.Model):
    """
    Переведення в штат
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='transfers')
    dismissal_date = models.DateField(verbose_name=_('Дата переведення'))
    order_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
    order_number = models.CharField(max_length=20, verbose_name='№ наказу')

    class Meta:
        verbose_name = _('Переведення в штат')
        verbose_name_plural = _('Переведення в штат')

    def __str__(self):
        return self.order_number


class Permission(models.Model):
    """
    Дозвіл на роботу
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='permissions')
    employer = models.CharField(max_length=40, verbose_name='Підприємство-роботодавець')
    factory = models.CharField(max_length=40, verbose_name='Завод')
    expire = models.DateField(verbose_name=_('Дата завершення'), null=True, blank=True)
    scan_copy = models.ImageField(verbose_name=_("Скан дозволу"), blank=True, null=True, upload_to="user/permission")

    class Meta:
        verbose_name = _('Дозвіл на роботу')
        verbose_name_plural = _('Дозволи на роботу')

    def __str__(self):
        return self.employer


class Vnosok(models.Model):
    """
    Вньоски
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='vnosok_list')
    employer = models.CharField(max_length=40, verbose_name='Підприємство-роботодавець')
    factory = models.CharField(max_length=40, verbose_name='Завод')
    position = models.CharField(max_length=40, verbose_name='Посада')
    start_on = models.DateField(verbose_name=_('Дата подачі'), null=True, blank=True)
    expire = models.DateField(verbose_name=_('Дата закриття'), null=True, blank=True)

    class Meta:
        verbose_name = _('Вньосок')
        verbose_name_plural = _('Вньоски')

    def __str__(self):
        return self.employer


class VocationType(models.Model):
    """
    Тип відпустки
    """
    title = models.CharField(max_length=40)

    class Meta:
        verbose_name = _('Тип відпустки')
        verbose_name_plural = _('Типи відпусток')

    def __str__(self):
        return self.title


    #TODO додати період для відпустки
class Vocation(models.Model):
    """
    Відпустка
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='vocations')
    type = models.ForeignKey(VocationType, on_delete=models.CASCADE, verbose_name=_('Тип відпустки'))
    agreement = models.BooleanField(_('Згода заводу'), default=False)
    start_on = models.DateField(verbose_name=_('Дата початку відпустки'), null=True, blank=True)
    expire = models.DateField(verbose_name=_('Дата закінчення відпустки'), null=True, blank=True)
    order_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
    order_number = models.CharField(max_length=20, verbose_name='№ наказу')
    comment = models.CharField(max_length=20, verbose_name='Примітки')

    class Meta:
        verbose_name = _('Відпустка')
        verbose_name_plural = _('Відпустки')

    def __str__(self):
        return self.type.title


class IncomingControl(models.Model):
    """
     Вхідний контроль
    """
    user = models.OneToOneField('user_profile.User', on_delete=models.CASCADE, related_name='incoming_controls')
    factory = models.CharField(max_length=40, verbose_name='Завод')
    expire = models.DateField(verbose_name=_("Дата від'їзду"), null=True, blank=True)

    class Meta:
        verbose_name = _('Вхідний контроль')
        verbose_name_plural = _('Вхідні контролі')

    def __str__(self):
        return self.factory


class Prognosis(models.Model):
    """
     Прогноз
    """
    user = models.OneToOneField('user_profile.User', on_delete=models.CASCADE, related_name='prognoses')
    reason = models.CharField(max_length=40, verbose_name='Причина повернення')
    expire = models.DateField(verbose_name=_("Дата прибуття"), null=True, blank=True)
    agree = models.BooleanField(_('Згода заводу'), default=False)

    class Meta:
        verbose_name = _('Прогноз')
        verbose_name_plural = _('Прогнози')

    def __str__(self):
        return self.reason


class Disappearance(models.Model):
    """
     Зникнення
    """
    user = models.OneToOneField('user_profile.User', on_delete=models.CASCADE, related_name='disappearances')
    violation_date = models.DateField(verbose_name=_("Дата порушення"), null=True, blank=True)
    appeal_date = models.DateField(verbose_name=_("Дата звернення"), null=True, blank=True)

    class Meta:
        verbose_name = _('Зникнення')
        verbose_name_plural = _('Зникнення')

    def __str__(self):
        return self.violation_date
