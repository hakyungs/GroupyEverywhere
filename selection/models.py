from django.db import models

# Create your models here.
class Selection(models.Model):
    category = models.CharField(max_length=10)

    def __str__(self):
        return self.category