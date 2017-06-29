from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class User:
    id = None
    name = None
    email = None
    phone = None
    mobile_phone = None
    status = None
    courses = None

    def __init__(self, name, email, status):
        self.name = name
        self.email = email
        self.status = status

    def __str__(self):
        return id

    class Meta:
        ordering = ('user_id',)


class PassObject:
    model_form_type = None
    html = None
    entity_from_db = None
    redirect_uri = None

    def default_user_vals(self, model_form_type):
        self.model_form_type = model_form_type
        self.html = 'tz/user_create.html'
        self.redirect_uri = '/users/'

    def default_course_vals(self, model_form_type):
        self.model_form_type = model_form_type
        self.html = 'tz/course_create.html'
        self.redirect_uri = '/courses/'


class LoggedUser(object):
    __user = None
    __instance = None

    @staticmethod
    def instance(user):
        if LoggedUser.__instance is None:
            LoggedUser.__instance = LoggedUser(user)
        return LoggedUser.__instance

    def __init__(self, user):
        self.__user = user

    def get_user(self):
        return self.__user
