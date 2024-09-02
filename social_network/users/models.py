from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.db import models




class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    name = models.CharField('name', max_length=20, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name




friend_req_status = [('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')]

class FriendRequest(models.Model):
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_requests')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=10, choices=friend_req_status)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s (%s)' % (self.from_user, self.to_user, self.status)




