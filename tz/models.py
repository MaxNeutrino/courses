from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class UserAdditional(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    mobile_phone = models.CharField(max_length=15)
    courses = models.ManyToManyField(Course)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user_id

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
