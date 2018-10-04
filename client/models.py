from django.db import models


class Document(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    bio = models.TextField()
    photo = models.FileField(null=True, blank=True)
    doc = models.OneToOneField(Document, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Product(models.Model):
    description = models.CharField(max_length=7)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.description


class Sale(models.Model):
    number = models.CharField(max_length=7)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    taxes = models.DecimalField(max_digits=5, decimal_places=2)
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.number

