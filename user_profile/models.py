from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext as _
from user_profile.managers import UserManager


class ContactType(models.Model):
    """
    Тип контактов пользователя
    """
    title = models.CharField(max_length=40, verbose_name=_('Тип контакта'))

    class Meta:
        verbose_name = _('Тип контакта')
        verbose_name_plural = _('Типи контактів')

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    Контакти пользователя
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='contacts')
    type = models.ForeignKey(ContactType, on_delete=models.CASCADE, verbose_name=_('Тип контакта'))
    contact = models.CharField(max_length=20, verbose_name=_('Контакт'))
    sort = models.PositiveSmallIntegerField(default=1, verbose_name=_('Порядок сортування'))

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакти')
        ordering = ['sort']

    def __str__(self):
        return self.contact


class IntelligenceType(models.Model):
    """
    Інтелект працівника
    """
    title = models.CharField(max_length=40, verbose_name=_('Інтелект'))

    class Meta:
        verbose_name = _('Інтелект')
        verbose_name_plural = _('Інтелект')

    def __str__(self):
        return self.title


class ProfessionalismType(models.Model):
    """
    Професіоналізм працівника
    """
    title = models.CharField(max_length=40, verbose_name=_('Професіоналізм'))

    class Meta:
        verbose_name = _('Професіоналізм')
        verbose_name_plural = _('Професіоналізм')

    def __str__(self):
        return self.title


class SelfDiscipline(models.Model):
    """
    Самодисциплінованість працівника
    """
    title = models.CharField(max_length=40, verbose_name=_('Самодисциплінованість'))

    class Meta:
        verbose_name = _('Самодисциплінованість')
        verbose_name_plural = _('Самодисциплінованість')

    def __str__(self):
        return self.title


class SociabilityType(models.Model):
    """
    Комунікабельність працівника
    """
    title = models.CharField(max_length=40, verbose_name=_('Комунікабельність'))

    class Meta:
        verbose_name = _('Комунікабельність')
        verbose_name_plural = _('Комунікабельність')

    def __str__(self):
        return self.title


class TemperamentType(models.Model):
    """
    Темперамент працівника
    """
    title = models.CharField(max_length=40, verbose_name=_('Темперамент'))

    class Meta:
        verbose_name = _('Темперамент')
        verbose_name_plural = _('Темперамент')

    def __str__(self):
        return self.title


class PersonalityType(models.Model):
    """
    Тип особистості працівника
    """
    title = models.CharField(max_length=40, verbose_name=_('Тип особистості'))

    class Meta:
        verbose_name = _('Тип особистості')
        verbose_name_plural = _('Типи особистості')

    def __str__(self):
        return self.title


class PsychologicalPortrait(models.Model):
    """
    Психологічний портрет користувача
    """
    user = models.OneToOneField('user_profile.User', on_delete=models.CASCADE, related_name='portraits')
    intelligence = models.ForeignKey(IntelligenceType, on_delete=models.CASCADE,
                                     null=True, blank=True, verbose_name=_('Інтелект'))
    professionalism = models.ForeignKey(ProfessionalismType, on_delete=models.CASCADE,
                                        null=True, blank=True, verbose_name=_('Професіоналізм'))
    self_discipline = models.ForeignKey(SelfDiscipline, on_delete=models.CASCADE,
                                        null=True, blank=True, verbose_name=_('Самодисципліна'))
    sociability = models.ForeignKey(SociabilityType, on_delete=models.CASCADE,
                                    null=True, blank=True, verbose_name=_('Комунікабельність'))
    temperament = models.ForeignKey(TemperamentType, on_delete=models.CASCADE,
                                    null=True, blank=True, verbose_name=_('Темперамент'))
    personality_type = models.ForeignKey(PersonalityType, on_delete=models.CASCADE,
                                         null=True, blank=True, verbose_name=_('Тип особистості'))

    class Meta:
        verbose_name = _('Психологічний портрет')
        verbose_name_plural = _('Психологічні портрети')

    # def __str__(self):
    #     return self.contact


class Status(models.Model):
    """
    Статуси пользователя
    """
    status = models.CharField(max_length=30, verbose_name=_('Статус'))

    class Meta:
        verbose_name = _('Статус')
        verbose_name_plural = _('Статуси')

    def __str__(self):
        return self.status


class Position(models.Model):
    """
    Список посад
    """
    title = models.CharField(max_length=60, verbose_name=_('Посада'))

    class Meta:
        verbose_name = _('Посада')
        verbose_name_plural = _('Посади')

    def __str__(self):
        return self.title


class LanguageTitle(models.Model):
    """
    Список мов
    """
    title = models.CharField(max_length=60, verbose_name=_('Мова'))

    class Meta:
        verbose_name = _('Список мов')
        verbose_name_plural = _('Списки мов')

    def __str__(self):
        return self.title


class LanguageLevel(models.Model):
    """
    Рівень володіння
    """
    title = models.CharField(max_length=60, verbose_name=_('Рівень'))

    class Meta:
        verbose_name = _('Рівень володіння')
        verbose_name_plural = _('Рівні володіння')

    def __str__(self):
        return self.title


class Language(models.Model):
    """
    Мови якими володіє користувач
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, related_name='languages')
    title = models.ForeignKey(LanguageTitle, on_delete=models.CASCADE, verbose_name=_('Мова'), related_name='languages')
    level = models.ForeignKey(LanguageLevel, on_delete=models.CASCADE, verbose_name=_('Рівень'), related_name='languages')

    class Meta:
        verbose_name = _('Мова')
        verbose_name_plural = _('Мови')

    def __str__(self):
        return self.title


class User(AbstractBaseUser, PermissionsMixin):
    """
    Пользователи системы
    """
    email = models.EmailField(verbose_name=_('email'), max_length=255, unique=True, null=True, blank=True)
    avatar = models.ImageField(verbose_name=_('Аватар'), blank=True, null=True, upload_to="user/avatar")
    first_name = models.CharField(verbose_name=_('Прізвище'), max_length=40)
    last_name = models.CharField(verbose_name=_("Ім'я"), max_length=40)
    patronymic = models.CharField(verbose_name=_('По-батькові'), max_length=40)
    registration = models.CharField(verbose_name=_("Адреса прописки"), max_length=200, blank=True)
    residence_address = models.CharField(verbose_name=_('Фактична адреса'), max_length=200, blank=True)
    # login = models.CharField(max_length=30, verbose_name=_('Логін'), unique=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Дата народження', null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name=_('Посада'), null=True, blank=True)
    status = models.ForeignKey('user_profile.Status', on_delete=models.CASCADE, verbose_name=_('Статус'),
                               related_name='user', null=True, blank=True)
    note = models.TextField(verbose_name=_('Примітки'), max_length=1000, null=True, blank=True)
    is_admin = models.BooleanField(_('Суперюзер'), default=False)
    is_worker = models.BooleanField(_('Клієнт'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = _('Користувач')
        verbose_name_plural = _('Користувачі')

    def __str__(self):
        if self.email:
            return self.email
        else:
            return '{} {}.{}.'.format(self.first_name, self.last_name[0].upper(), self.patronymic[0].upper())

    @property
    def get_full_name(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.patronymic)

    @property
    def get_full_name_short(self):
        return '{} {}.{}.'.format(self.first_name, self.last_name[0].upper(), self.patronymic[0].upper())

    @property
    def is_staff(self):
        return self.is_admin
