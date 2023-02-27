from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


def cin_length(v):
    if len(str(v)) != 8:
        raise ValidationError("your cin must have 8 chara!!")
    return v


def mail_esprit(mm):
    if str(mm).endswith('@esprit.tn') == False: raise ValidationError('your email -{m} -must end with esprit.tn'
                                                                      , params={"m": mm})


# Create your models here.
class Person(AbstractUser):
    cin = models.IntegerField('CIN',
                              primary_key=True, validators=[MaxValueValidator(99999999), MinValueValidator(10**7), cin_length])
    email = models.EmailField(validators=[mail_esprit])

# class Meta:
#     verbose_name_plural="users"