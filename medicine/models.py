from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.


class InsuranceType(models.Model):
    """
    Тип страхування
    """
    title = models.CharField(max_length=40, verbose_name='Тип страхування')

    class Meta:
        verbose_name = _('Тип страхування')
        verbose_name_plural = _('Типы страхування')

    def __str__(self):
        return self.title


class InsuranceEvent(models.Model):
    """
    Страхова подія
    """
    title = models.CharField(max_length=40, verbose_name='Страхова подія')
    expire = models.DateField(verbose_name='Дата завершення', null=True, blank=True)
    insurance = models.ForeignKey('medicine.Insurance', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Страхова подія')
        verbose_name_plural = _('Страхові події')

    def __str__(self):
        return self.title


class Insurance(models.Model):
    """
    Страхуванн
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE)
    insurance_organization = models.CharField(max_length=20, verbose_name=_('Страхова організація'))
    type = models.ForeignKey(InsuranceType, on_delete=models.CASCADE, verbose_name=_('Тип страхування'))
    expire = models.DateField(verbose_name='Дата завершення', null=True, blank=True)
    scan_copy = models.ImageField(verbose_name=_('Скан страхування'), blank=True, null=True, upload_to="user/insurance")

    class Meta:
        verbose_name = _('Страхування')
        verbose_name_plural = _('Страхування')

    def __str__(self):
        return '{} - {}'.format(self.type, self.expire)


class MedicalReviewType(models.Model):
    """
    Тип медогляду
    """
    title = models.CharField(max_length=40, verbose_name='Тип медогляду')
    expire = models.DateField(verbose_name='Дата завершення', null=True, blank=True)

    class Meta:
        verbose_name = _('Тип медогляду')
        verbose_name_plural = _('Типы медогляду')

    def __str__(self):
        return self.title


class MedicalReview(models.Model):
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE)
    type = models.ForeignKey(MedicalReviewType, on_delete=models.CASCADE, verbose_name=_('Тип медогляду'))
    early_expire = models.DateField(verbose_name='Дострокове завершення', null=True, blank=True)
    has_review = models.BooleanField(verbose_name=_('Наявність медогляду'), default=False)

    class Meta:
        verbose_name = _('Медогляд')
        verbose_name_plural = _('Медогляди')

    def __str__(self):
        return self.has_review
