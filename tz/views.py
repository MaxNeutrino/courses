from django.views import generic

from tz.models import User, Course


class UserView(generic.ListView):
    model = User
    template_name = 'tz/users.html'
    context_object_name = 'user_model_list'

    def get_queryset(self):
        return User.objects.all()


class CourseView(generic.ListView):
    model = Course
    template_name = "tz/courses.html"
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.all()
