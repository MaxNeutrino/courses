from django.contrib import admin

from tz.models import Course, User, UserAdditional

admin.site.register(Course)
admin.site.register(UserAdditional)
