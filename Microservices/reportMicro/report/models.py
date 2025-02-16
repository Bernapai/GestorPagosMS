from django.db import models

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title