from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    mobile_phone = models.CharField(max_length=15)
    courses = models.ManyToManyField(Course)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('name',)
