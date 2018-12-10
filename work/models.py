from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.


class BasisList(models.Model):
    """
    Список підстав
    """
    title = models.CharField(max_length=60, verbose_name=_('Підстава звільнення'))

    class Meta:
        verbose_name = _('Підстава звільнення')
        verbose_name_plural = _('Підстави звільнення')

    def __str__(self):
        return self.title


class Dismissal(models.Model):
    """
    Звільнення
    """
    user = models.OneToOneField('user_profile.User', on_delete=models.CASCADE, related_name='dismissals')
    dismissal_date = models.DateField(verbose_name=_('Дата звільнення'), null=True, blank=True)
    order_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
    order_number = models.CharField(max_length=40, verbose_name='№ наказу', null=True, blank=True)
    dismissal_reason = models.CharField(max_length=40, verbose_name='Причина звільнення', null=True, blank=True)
    dismissal_basis = models.ForeignKey(BasisList, on_delete=models.CASCADE, related_name='dismissals', verbose_name='Підстава звільнення')

    class Meta:
        verbose_name = _('Звільнення')
        verbose_name_plural = _('Звільнення')

    def __str__(self):
        return self.order_number
#
#
# class AssignmentNote(models.Model):
#     """
#     Примітки по відрядженню
#     """
#     title = models.CharField(max_length=200)
#     order_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
#     order_number = models.CharField(max_length=40, verbose_name='№ наказу')
#
#     class Meta:
#         verbose_name = _('Примітка')
#         verbose_name_plural = _('Примітки')
#
#     def __str__(self):
#         return self.title


class Assignment(models.Model):
    """
    Відрядження
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='assignments')
    order_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
    order_number = models.CharField(max_length=40, verbose_name='№ наказу', null=True, blank=True)
    factory = models.ForeignKey('work.Factory', on_delete=models.CASCADE, related_name='assignment', verbose_name='Завод')
    city = models.CharField(max_length=40, verbose_name='Місто відрядження', null=True, blank=True)
    start_on = models.DateField(verbose_name=_('Початок відрядження'), null=True, blank=True)
    expire = models.DateField(verbose_name=_('Закінчення відрядження'), null=True, blank=True)
    polish_border = models.DateField(verbose_name=_('Перетин кордону в Польщу'), null=True, blank=True)
    ukrainian_border = models.DateField(verbose_name=_('Перетин кордону в Україну'), null=True, blank=True)
    dismissal_reason = models.CharField(max_length=200, verbose_name='Причина дострокове закінчення', null=True, blank=True)
    reason_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
    reason_number = models.CharField(max_length=40, verbose_name='№ наказу', null=True, blank=True)
    dismissal_basis = models.CharField(max_length=200, verbose_name='Причина переривання відрядження', null=True, blank=True)
    basis_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
    basis_number = models.CharField(max_length=40, verbose_name='№ наказу', null=True, blank=True)

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
    dismissal_date = models.DateField(verbose_name=_('Дата прийняття'), null=True, blank=True)
    order_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
    order_number = models.CharField(max_length=20, verbose_name='№ наказу', null=True, blank=True)
    employer = models.ForeignKey('work.Employer', on_delete=models.CASCADE, related_name='adoptions', verbose_name='Підприємство-роботодавець')
    # factory = models.CharField(max_length=40, verbose_name='Завод')
    position = models.ForeignKey('user_profile.Position', on_delete=models.CASCADE, verbose_name=_('Посада'), null=True,
                                 blank=True)

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
    dismissal_date = models.DateField(verbose_name=_('Дата переведення'), null=True, blank=True)
    order_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
    order_number = models.CharField(max_length=20, verbose_name='№ наказу', null=True, blank=True)
    position = models.ForeignKey('user_profile.Position', on_delete=models.CASCADE, verbose_name=_('Посада'), null=True, blank=True)

    class Meta:
        verbose_name = _('Переведення в штат')
        verbose_name_plural = _('Переведення в штат')

    def __str__(self):
        return self.order_number


class Voivodship(models.Model):
    """
    Список воєводств
    """
    title = models.CharField(max_length=60, verbose_name=_('Воєводство'))

    class Meta:
        verbose_name = _('Воєводство')
        verbose_name_plural = _('Воєводства')

    def __str__(self):
        return self.title


class Employer(models.Model):
    """
    Список роботодавців
    """
    title = models.CharField(max_length=60, verbose_name=_('Підприємство-роботодавець'))

    class Meta:
        verbose_name = _('Підприємство-роботодавець')
        verbose_name_plural = _('Підприємства-роботодавці')

    def __str__(self):
        return self.title


class Factory(models.Model):
    """
    Список заводів
    """
    title = models.CharField(max_length=60, verbose_name=_('Завод'))

    class Meta:
        verbose_name = _('Завод')
        verbose_name_plural = _('Заводи')

    def __str__(self):
        return self.title


class Permission(models.Model):
    """
    Дозвіл на роботу
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='permissions')
    pay_date = models.DateField(verbose_name='Дата оплати', null=True, blank=True)
    prediction_date = models.DateField(verbose_name=_('Дата відправлення внеску'), null=True, blank=True)
    input_date = models.DateField(verbose_name=_('Дата подачі внеск'), null=True, blank=True)
    receiving_date = models.DateField(verbose_name=_('Прогнозована дата отримання дозволу'), null=True, blank=True)
    voivodship = models.ForeignKey(Voivodship, on_delete=models.CASCADE, related_name='permissions', verbose_name='Воєводство')
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='permissions', verbose_name='Підприємство-роботодавець')
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='permissions', verbose_name='Завод')
    start_date = models.DateField(verbose_name=_('Дата початку'), null=True, blank=True)
    expire = models.DateField(verbose_name=_('Дата завершення'), null=True, blank=True)
    note = models.CharField(max_length=400, verbose_name='Примітки', null=True, blank=True)
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
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='vnosok_list',
                                 verbose_name='Підприємство-роботодавець')
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='vnosok_list', verbose_name='Завод')
    position = models.CharField(max_length=60, verbose_name='Посада')
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
    period = models.CharField(max_length=60, verbose_name='Період для відпустки', null=True, blank=True)
    start_on = models.DateField(verbose_name=_('Дата початку відпустки'), null=True, blank=True)
    expire = models.DateField(verbose_name=_('Дата закінчення відпустки'), null=True, blank=True)
    order_date = models.DateField(verbose_name=_('Дата наказу'), null=True, blank=True)
    order_number = models.CharField(max_length=20, verbose_name='№ наказу', null=True, blank=True)
    comment = models.CharField(max_length=400, verbose_name='Примітки', null=True, blank=True)

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
    factory = models.ForeignKey('work.Factory', on_delete=models.CASCADE, related_name='incoming_controls', verbose_name='Завод')
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
    reason = models.CharField(max_length=400, verbose_name='Причина повернення', null=True, blank=True)
    expire = models.DateField(verbose_name=_("Дата прибуття"), null=True, blank=True)
    agree = models.BooleanField(_('Згода заводу'), default=False)

    class Meta:
        verbose_name = _('Прогноз')
        verbose_name_plural = _('Прогнози')

    def __str__(self):
        if self.agree:
            return "Погоджено з заводом"
        else:
            return "Не погоджено"


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
