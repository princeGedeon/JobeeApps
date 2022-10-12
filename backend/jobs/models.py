from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class JobType(models.TextChoices):
    Permanent="Permanent"
    Temporaty="Temporary"
    Phd='Phd'

class Education(models.TextChoices):
    Bachelors="Bachelors"
    Masters="Masters"
    Phd="Phd"


class Industry(models.TextChoices):
    Business="Busness"
    IT="Information Technilogy"
    Education="Education"
    Others="Others"

class Experience(models.TextChoices):
    NO_EXPERIENCE="No experience"
    ONE_YEAR="1 Year"
    TWO_YEAR='2 Year'
    THREE_YEARS_PLUS="3 Years above"

def return_date():
    now=datetime.now()
    return now + timedelta(days=10)

class Job(models.Model):
    title=models.CharField(max_length=200,null=True)
    desctiption=models.TextField(null=True)
    email=models.EmailField(null=True)
    adress=models.CharField(max_length=100,null=True)
    jobType=models.CharField(
        max_length=45,
        choices=JobType.choices,
        default=JobType.Permanent
    )
    education = models.CharField(
        max_length=45,
        choices=Education.choices,
        default=Education.Bachelors
    )
    industry = models.CharField(
        max_length=45,
        choices=Industry.choices,
        default=Industry.Business
    )
    experience = models.CharField(
        max_length=45,
        choices=Experience.choices,
        default=Experience.NO_EXPERIENCE
    )

    salary=models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(1000000000)])
    company=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now_add=True)
    last_date=models.DateTimeField(default=return_date)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title