from django.views import generic

from tz.models import User, Course


class UserView(generic.ListView):
    model = User
    template_name = 'tz/users.html'

    def get_queryset(self):
        return User.objects


class CourseView(generic.ListView):
    model = Course
    template_name = "tz/courses.html"

    def get_queryset(self):
        return Course.objects
