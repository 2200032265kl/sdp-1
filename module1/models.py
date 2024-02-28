from django.db import models

class Akhila(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=100)
    class Meta:
        db_table="Akhila"


class Akhilaa(models.Model):
    firstname=models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    comments=models.CharField(max_length=400)
    class Meta:
        db_table="Akhilaa"

