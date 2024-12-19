from django.db import models

# Create your models here.


class Persons(models.Model):

    name = models.CharField(max_length=50)  # username аккаунта
    grade = models.CharField(max_length=20)
    age = models.IntegerField()
    password = models.CharField(max_length=20, default='12345678')

    def __str__(self):
        return self.name


class Text_to_stady(models.Model):
    title = models.CharField(max_length=50)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    original_url = models.CharField(max_length=50)
    stady = models.ManyToManyField(Persons, related_name='text')

    def __str__(self):
        return self.title

class Video_to_stady(models.Model):
    title = models.CharField(max_length=50)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    original_url = models.CharField(max_length=50)
    stady = models.ManyToManyField(Persons, related_name='video')

    def __str__(self):
        return self.title

class Tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.IntegerField()
    buyer = models.ManyToManyField(Persons, related_name='tasks')

    def __str__(self):
        return self.title