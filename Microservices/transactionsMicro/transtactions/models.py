from django.db import models

# Create your models here.
class Transaction(models.Model):
    user_id = models.IntegerField()
    amount = models.FloatField()
    date = models.DateField()
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)