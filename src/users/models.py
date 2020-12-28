import uuid
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):

    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username_validator = UnicodeUsernameValidator()
    
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    email = models.EmailField(_('email address'), unique=True)
    
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'User'
        verbose_name = _('user')
        verbose_name_plural = _('ユーザー')
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # class Meta:
    #     db_table = 'User'
    #     verbose_name_plural = 'ユーザのモデル'
    
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # family_name = models.CharField(verbose_name = '姓', max_length=10)
    # first_name = models.CharField(verbose_name = '名', max_length=10)
    # family_name_kana = models.CharField(verbose_name = '姓（かな）', max_length=20)
    # first_name_kana = models.CharField(verbose_name = '名（かな）', max_length=20)
    # old_family_name = models.CharField(verbose_name = '旧姓', max_length=20, null=True)
    # old_family_name_kana = models.CharField(verbose_name = '旧姓（かな）', max_length=20, null=True)
    
    # sex = models.CharField(verbose_name='性別', max_length=2, choices=(('男性','男性'), ('女性','女性')))
    # birthday = models.DateTimeField(verbose_name='生年月日', null=True)
    # email = models.EmailField(verbose_name='メールアドレス', max_length=100)
    
    # country = models.CharField(verbose_name='国', default='日本', max_length=15, editable=False)
    # postal_code = models.SmallIntegerField(verbose_name='郵便番号（ハイフンなし）', null=True)
    # prefecture = models.CharField(verbose_name = '都道府県', max_length=5, null=True)
    # address = models.CharField(verbose_name = '住所', max_length=50, null=True)
    # building = models.CharField(verbose_name = '建物名', max_length=30, null=True)
    # tel = models.SmallIntegerField(verbose_name='電話番号（ハイフンなし）', null=True)
    
    # url = models.URLField(verbose_name='URL', max_length=300, null=True)
    # photo = models.ImageField(verbose_name='写真', null=True)

    # created_at = models.DateTimeField(default=timezone.now, editable=False)
    # last_updated = models.DateTimeField(auto_now=True, editable=False)

    # USERNAME_FIELD = 'email'

    # def __str__(self):
    #     return self.family_name + ' ' + self.first_name
