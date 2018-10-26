from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

# from user_profile.models import User


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_("Необхідно обов'язково вказати Email"))

        user = self.model(
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        # result = re.findall(r'^(\w+)@', email)
        # # id = User.
        # user.login = result[0]+'1'
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return
