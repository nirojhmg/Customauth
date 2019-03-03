from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Batch(models.Model):
    class Meta:
        verbose_name='batche'
    Batch_type = models.CharField(max_length=30)
    Year = models.CharField(max_length=30)
    
class Student(models.Model):
    FirstName = models.CharField(max_length=30)
    MiddleName = models.CharField(max_length=30,blank=True,null=True)
    LastName = models.CharField(max_length=30)
    FatherName=models.CharField(max_length=150)
    Branch=models.CharField(max_length=50)
    Course=models.CharField(max_length=150)
    Date_of_Birth=models.DateField()
    Batch=models.ForeignKey('Batch',on_delete=models.CASCADE)
    User_id=models.ForeignKey('MyUser',on_delete=models.CASCADE)
    
class Faculty(models.Model):
    FirstName = models.CharField(max_length=30)
    MiddleName = models.CharField(max_length=30,blank=True,null=True)
    LastName = models.CharField(max_length=30)   
    Date_of_Birth=models.DateField()
    FacultyType = models.CharField(max_length=30)   
    User_id=models.ForeignKey('MyUser',on_delete=models.CASCADE)
    


    
class MyUserManager(BaseUserManager):
    def create_user(self, email,  password,FirstName,MiddleName,LastName,is_student):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            FirstName=FirstName,
            MiddleName=MiddleName,
            LastName=LastName,
            is_student=is_student
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password,FirstName,MiddleName,LastName,is_student):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            FirstName=FirstName,
            MiddleName=MiddleName,
            LastName=LastName,
            is_student=is_student
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=50,
        unique=True,
    )
    FirstName = models.CharField(
        verbose_name='First name',
        max_length=50,
    )
    MiddleName = models.CharField(
        verbose_name='Middle name',
        max_length=50,
        null=True
        
    )
    LastName = models.CharField(
        verbose_name='Last name',
        max_length=50,
    )
    is_student=models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['FirstName','MiddleName','LastName','is_student']

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

 