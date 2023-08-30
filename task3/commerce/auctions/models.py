from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction(models.Model):
    title = models.CharField(
        unique=True, error_messages={'unique': "The auction with that title already exists."},
        max_length=64, verbose_name='title of auction')
    category = models.CharField(max_length=64)
    description = models.CharField(blank=True, max_length=124)
    image_url = models.CharField(blank=True, max_length=124)
    price = models.FloatField(default=0.0)
    owner = models.CharField(max_length=64)  # user
    winner = models.CharField(blank=True, max_length=64)  # user
    is_active = models.BooleanField(default=False, verbose_name='active status')  # active or non_active


class Bet(models.Model):
    title = models.CharField(max_length=64)  # auction
    user = models.CharField(max_length=64)  # user
    price = models.FloatField()


class Comment(models.Model):
    title = models.CharField(max_length=64)  # auction
    user = models.CharField(max_length=64)  # user
    comments = models.CharField(max_length=128)


class Watchlist(models.Model):
    user = models.CharField(max_length=64)  # user
    title = models.CharField(max_length=64)  # auction