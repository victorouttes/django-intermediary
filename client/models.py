from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    bio = models.TextField()
    photo = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
