from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext as _
from user_profile.managers import UserManager


class ContactType(models.Model):
    """
    Тип контактов пользователя
    """
    title = models.CharField(max_length=40)
    validate_string = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = _('Тип контакта')
        verbose_name_plural = _('Типи контактів')

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    Контакти пользователя
    """
    user = models.ForeignKey('user_profile.User', on_delete=models.CASCADE)
    type = models.ForeignKey(ContactType, on_delete=models.CASCADE, verbose_name=_('Тип контакта'))
    contact = models.CharField(max_length=20, verbose_name=_('Контакт'))
    sort = models.PositiveSmallIntegerField(default=1, verbose_name=_('Порядок сортування'))

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакти')
        ordering = ['sort']

    def __str__(self):
        return self.contact

    def save(self, *args, **kwargs):
        # TODO Зробити валідацію контактних даних
        re_string = self.type.validate_string
        if re_string:
            pass
        return super(Contact, self).save(*args, **kwargs)


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


class User(AbstractBaseUser, PermissionsMixin):
    """
    Пользователи системы
    """
    email = models.EmailField(verbose_name=_('email'), max_length=255, unique=True, db_index=True)
    avatar = models.ImageField(verbose_name=_('Аватар'), blank=True, null=True, upload_to="user/avatar")
    first_name = models.CharField(verbose_name=_('Прізвище'), max_length=40)
    last_name = models.CharField(verbose_name=_("Ім'я"), max_length=40)
    patronymic = models.CharField(verbose_name=_('По-батькові'), max_length=40)
    login = models.CharField(max_length=30, verbose_name=_('Логін'), unique=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Дата народження', null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name=_('Посада'), null=True, blank=True)
    is_admin = models.BooleanField(_('Суперюзер'), default=False)
    is_worker = models.BooleanField(_('Клієнт'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = _('Користувач')
        verbose_name_plural = _('Користувачі')

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.patronymic)

    @property
    def get_full_name_short(self):
        return '{} {}.{}.'.format(self.first_name, self.last_name[0].upper(), self.patronymic[0].upper())

    @property
    def is_staff(self):
        return self.is_admin

#
# class Sex(models.Model):
#     sex = models.CharField()
#
#
# class Mobile(models.Model):
#     number =
#
#
# class Contacts(models.Model):
#     email = models.EmailField()
#     mobile = models.ForeignKey(Mobile)
#
#
# class User(models.Model):
#     full_name = models.CharField(max_length=250, verbose_name="ФИО")
#     sex = models.ForeignKey(Sex, on_delete=models.SET_NULL, verbose_name="Стать")
#     image = models.ImageField()
#     contacts = models.ForeignKey(Contacts)
#
#
# class Worker(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class Staff(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


# Працівник
# class Worker(models.modelsModel):
#     # first_name =
#     # surname =
#     # father_name =
#     full_name =
#     sex =
#     factory = # з моделі
#     contact =contact # з моделі


# # контактні дані
# class Contact(models.Model):
#
#
#
# # Віза
# #  перенести в модель працівника
# class Visa(models.Model):
#     start_on =
#     expire =
#
#
#
# # Дозвіл
# class Permission(models.Model):
#     start_on = models.DateField(verbose_name=_('hjhgjh'))
#     expire =
#     factory = # з моделі
#     provider_of_permission = # з моделі
#
#
#
# # Завод
# class Factory(models.Model):
#
#
#
#
# # надавач доступу
# class ProviderOfPermission(models.Model):
#
#
#
#
#
# # Сертифікат
# class Certificate(models.Model):
#     start_on =
#     expire =
#     welding_method =  # з моделі
#
#
#
# # Метод зварювання
# class WeldingMethod(models.Model):
#
#
#
# # Страхування
# class Insurance(models.Model):
#     start_on =
#     expire =
#     insurance_type =
#     insurance_organization = # з моделі
#
#
#
# # Страхова організація
# class InsuranceOrganization(models.Model):
#
#
#
# # Прийняття в штат
# class AdoptionInState(models.Model):
#     order_number =
#     order_date =
#     hiring_date =
#     transfer_in_state = # з моделі
#
#
#
#
# # переведення в межах штату
# class TransferInState(models.Model):
#     order_number =
#     order_date =
#     transfer_date =
#
#
#
# # Відрядження
# class Assignment(models.Model):
#     start_on =
#     expire =
#     order_number =
#     order_date =
#     date_of_departure =
#     date_or_return =
#     permission_from_the_factory =
#
#
#
# # Відпустки
# class Vacations(models.Model):
#     paid_vacation = # з моделі
#     unpaid_leave = # з моделі
#
#
#
# # Оплачуваний відпуск
# class PaidVacation(models.Model):
#     order_number =
#     order_date =
#     start_on =
#     expire =
#     days_count =
#     days_left = # calculate
#
#
#
# # Неоплачуваний відпуск
# class UnpaidLeave(models.Model):
#     order_number =
#     order_date =
#     start_on =
#     expire =
#     days_count =
#     days_left = # calculate
#
#
#
# # Медичний огляд
# class MedicalReview(models.Model):
#     has_review =
#     ua_review_date =
#     ua_review_expire =
#     pl_review_date =
#     pl_review_expire =
#     pl_review_loss =  # ???
#
#
#
# # Житло
# class Dwelling(models.Model):
#     """
#     fdjfdkjfdkjfkdfk dfsdjf skdjf
#     """
#     date_of_settlement =
#     date_of_eviction =        # same as
#
#
# # Звільнення
# class Dismissal(models.Model):
#
#
#
# # Інвалідність
# class Invalidity(models.Model):
#
