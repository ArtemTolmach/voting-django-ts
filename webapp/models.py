from datetime import timedelta

from django.db import models
from django.db.models import Max
from django.utils import timezone


class Character(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='characters/')
    age = models.IntegerField()
    biography = models.TextField()

    def __str__(self):
        return f"id:{self.id} SNP: {self.surname} {self.name} {self.patronymic}"


def get_default_end_date():
    return timezone.now() + timedelta(hours=1)


class Voting(models.Model):
    title = models.CharField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(default=get_default_end_date())
    max_voices = models.PositiveIntegerField()
    characters = models.ManyToManyField(Character, through='Vote')

    def is_active(self):
        return self.date_create < timezone.now() <= self.date_end and not any([i['voices'] >= self.max_voices for i in Vote.objects.filter(voting=self.id).values()])


class Vote(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    voices = models.PositiveIntegerField(default=0, editable=False)
    is_winner = models.BooleanField(default=False, editable=False)
