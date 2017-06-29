from django import forms

from tz.models import User, Course, UserAdditional


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = UserAdditional
        fields = "__all__"
        exclude = ('courses',)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserAdditional
        fields = "__all__"


class AuthForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(label='Password', max_length=32)


class RegistrationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=32)
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(label='Password', max_length=32)
    phone = forms.CharField(label='Phone')
    mobile_phone = forms.CharField(label='Mobile-Phone')
