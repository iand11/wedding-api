from django.db import models

# Create your models here.


class Guest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True)
    is_coming = models.BooleanField(default=False)
    people_attending = models.IntegerField(null=True)

    def __str__(self):
        return self.name
