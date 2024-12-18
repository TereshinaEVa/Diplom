from django.db import models

# Create your models here.



class Persons(models.Model):

    name = models.CharField(max_length=50)  # username аккаунта
    grade = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()
    password = hash(models.CharField())

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
    correct_ans = models.IntegerField()
    ball = models.IntegerField()
    buyer = models.ManyToManyField(Persons, related_name='tasks')

    def __str__(self):
        return self.title