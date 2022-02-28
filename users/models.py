from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from PIL import Image
import uuid

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, professional_training, phone, country, city, password=None,*args, **kwargs):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not email:
            raise ValueError('Users must have an email address!')

        if not username:
            raise ValueError('Users must have an username!')

        if not professional_training:
            raise ValueError('Users must have an professional_training!')

        if not phone:
            raise ValueError('Users must have an phone number!')

        if not country:
            raise ValueError('Users must set country!')

        if not city:
            raise ValueError('Users must set city!')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            professional_training = professional_training,
            phone = phone,
            country = country,
            city=city,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, professional_training, phone, country, city, password=None, *args, **kwargs):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
            professional_training = professional_training,
            phone = phone,
            country = country,
            city=city,


        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length = 25, unique=True)
    professional_training = models.CharField(max_length = 50)
    image = models.ImageField(verbose_name='Profile pic (leave empty for default pic)', default = 'default.jpg', upload_to = 'profile_pics')
    tk = models.CharField(default=uuid.uuid4(), unique=True,max_length=255, primary_key=True)
    phone = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    city = models.CharField(max_length=10)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','professional_training','phone','country','city']

    def save(self,*args, **kwargs): #resize the image if > 200x200
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin