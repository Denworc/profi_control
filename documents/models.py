from django.db import models
from django.utils.translation import ugettext as _
from user_profile.models import User

# Create your models here.


class UkrainianPassport(models.Model):
    series = models.CharField(max_length=2, verbose_name=_('Серія'), null=True)
    number = models.CharField(max_length=40, verbose_name=_('Номер паспорта'), blank=True)
    date_of_issue = models.DateField(verbose_name=_('Дата видачі'), null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pasports')
    surname = models.CharField(verbose_name=_('Прізвище'), max_length=40)
    last_name = models.CharField(verbose_name=_("Ім'я"), max_length=40)
    patronymic = models.CharField(verbose_name=_('По батькові'), max_length=40)
    place_of_issue = models.CharField(max_length=200, verbose_name=_('Ким був виданий'), blank=True)
    first_page = models.ImageField(verbose_name=_('2 сторінка'), blank=True, null=True, upload_to="user/ua_first")
    second_page = models.ImageField(verbose_name=_('3 сторінка'), blank=True, null=True, upload_to="user/ua_second")
    registration = models.ImageField(verbose_name=_('Прописка'), blank=True, null=True, upload_to="user/ua_registration")

    class Meta:
        verbose_name = _('Паспорт громадянина України')
        verbose_name_plural = _('Паспорти громадян України')

    def __str__(self):
        return '{} {}'.format(self.series.upper(), self.number)


class ForeignPassport(models.Model):
    number = models.CharField(max_length=6, verbose_name=_('Номер паспорта'), blank=True)
    date_of_issue = models.DateField(verbose_name=_('Дата видачі'), null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='foreign_pasport')
    surname = models.CharField(verbose_name=_('Прізвище'), max_length=40)
    last_name = models.CharField(verbose_name=_("Ім'я"), max_length=40)
    type = models.CharField(max_length=1, verbose_name=_('Тип'), blank=True)
    country_code = models.CharField(max_length=10, verbose_name=_('Код держави'), blank=True)
    authority = models.CharField(max_length=100, verbose_name=_('Орган, що видав'), blank=True)
    date_of_expiry = models.DateField(verbose_name=_('Дата закінчення строку дії'), null=True, blank=True)
    first_page = models.ImageField(verbose_name=_('1 сторінка'), blank=True, null=True, upload_to="user/foreign")

    class Meta:
        verbose_name = _('Закордонний паспорт')
        verbose_name_plural = _('Закордонні паспорта')

    def __str__(self):
        return self.number


class Visa(models.Model):
    """
    Віза пользователя
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='visas')
    visa_scan = models.ImageField(verbose_name=_('Скан копія'), blank=True, null=True, upload_to="user/visa")
    first_date = models.DateField(verbose_name=_('Дата подачі'), null=True, blank=True)
    prediction_date = models.DateField(verbose_name=_('Прогнозована дата отримання'), null=True, blank=True)
    start_on = models.DateField(verbose_name=_('Дата початку'), null=True, blank=True)
    expire = models.DateField(verbose_name=_('Дата закінчення строку дії'), null=True, blank=True)

    class Meta:
        verbose_name = _('Віза')
        verbose_name_plural = _('Візи')

    def __str__(self):
        return '{} - {}'.format(self.start_on, self.expire)


class MilitaryRecords(models.Model):
    """
    Військовий облік
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='military_records')
    start_on = models.DateField(verbose_name=_('Дата взяття на облік'), null=True, blank=True)
    expire = models.DateField(verbose_name=_('Дата зняття з обліку'), null=True, blank=True)

    class Meta:
        verbose_name = _('Військовий облік')
        verbose_name_plural = _('Військові обліки')

    def __str__(self):
        return '{} - {}'.format(self.start_on, self.expire)


class PersonalID(models.Model):
    """
    Ідентифікаційний код
    """
    user = models.OneToOneField('user_profile.User', on_delete=models.CASCADE, related_name='personal_id')
    personal_id = models.CharField(max_length=10, verbose_name=_('Ідентифікаційний код'), unique=True, blank=True)
    scan_id = models.ImageField(verbose_name=_('Скан копія'), blank=True, null=True, upload_to="user/id")

    class Meta:
        verbose_name = _('Ідентифікаційний код')
        verbose_name_plural = _('Ідентифікаційні коди')

    def __str__(self):
        return self.personal_id
