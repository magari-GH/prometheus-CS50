from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class Transaction(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="transactions")
    type = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    amount = models.FloatField(default=0)
    currency = models.CharField(max_length=3)
    date = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        # function serializing model's fuilds for use by JSON
        return {
            "id": self.id,
            "user": self.user.username,
            "category": self.category,
            "title": self.title,
            "amount": self.amount,
            "currency": self.currency,
            "date": self.date.strtime("%b %d %Y, %I:%M %p"),

        }
    
    def __str__(self):
        return f'Transaction {self.id} of the {self.user} category {self.category} title {self.title} in the {self.amount} {self.currency} on {self.date}'


class Account(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="accounts")
    title = models.CharField(max_length=64)
    amount = models.FloatField(default=0)
    currency = models.CharField(max_length=3)

    def serialize(self):
        # function serializing model's fuilds for use by JSON
        return {
            "id": self.id,
            "user": self.user.username,
            "title": self.title,
            "amount": self.amount,
            "currency": self.currency,
        }
    
    def __str__(self):
        return f'Account number {self.id} of the {self.user} called {self.title} current total is {self.amount} {self.currency}'

    


