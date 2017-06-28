from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from service.model_form_factory import ModelFormFactory, ModelFormType
from tz.forms import AuthForm, RegistrationForm
from tz.models import User, Course, PassObject, LoggedUser


class UserView(generic.ListView):
    model = User
    template_name = 'tz/users.html'
    context_object_name = 'user_model_list'

    def get_queryset(self):
        return User.objects.all()


class CourseView(generic.ListView):
    model = Course
    template_name = "tz/courses.html"
    context_object_name = 'course_model_list'

    def get_queryset(self):
        return Course.objects.all()


def auth(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is None:
                return redirect('/')

            record = User.objects.filter(
                email=username
            )

            if record is None:
                return redirect('/')

            logged_user = LoggedUser.instance(record)
    else:
        form = AuthForm()

    return render(request, 'tz/index.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            status = form.cleaned_data['status']

            user = User.objects.create_user(username=username, email=username, password=password, name=name, is_active=status)
            user.save()

            return redirect('/courses/')

    else:
        form = RegistrationForm()
    return render(request, 'tz/registration.html', {'form': form})


def delete_a_course(request, course_id):
    record = get_object_or_404(Course, pk=course_id)
    record.delete()
    return redirect('/courses/')


def delete_a_user(request, user_id):
    record = get_object_or_404(User, pk=user_id)
    record.delete()
    return redirect('/users/')


def create_a_course(request):
    pass_obj = PassObject()
    pass_obj.default_course_vals(ModelFormType.COURSE)

    return create_a_model(pass_obj, request)


def create_a_user(request):
    pass_obj = PassObject()
    pass_obj.default_user_vals(ModelFormType.USER_CREATE)

    return create_a_model(pass_obj, request)


def update_a_course(request, course_id):
    pass_obj = PassObject()
    pass_obj.default_course_vals(ModelFormType.COURSE)

    pass_obj.entity_from_db = get_object_or_404(Course, pk=course_id)

    return create_a_model(pass_obj, request)


def update_a_user(request, user_id):
    pass_obj = PassObject()
    pass_obj.default_user_vals(ModelFormType.USER_UPDATE)

    pass_obj.entity_from_db = get_object_or_404(User, pk=user_id)

    return create_a_model(pass_obj, request)


def create_a_model(pass_obj, request):
    if request.method == 'POST':
        form = ModelFormFactory.create_model_form(pass_obj.model_form_type,
                                                  request.POST,
                                                  pass_obj.entity_from_db)
        if form.is_valid():
            form.save()
            return redirect(pass_obj.redirect_uri)
    else:
        form = ModelFormFactory.create_model_form(pass_obj.model_form_type,
                                                  None,
                                                  pass_obj.entity_from_db)

    context_data = {'form': form}
    return render(request, pass_obj.html, context_data)
