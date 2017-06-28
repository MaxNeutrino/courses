from enum import Enum

from tz.forms import UserCreateForm, UserUpdateForm, CourseForm


class ModelFormType(Enum):
    USER_CREATE = 0
    USER_UPDATE = 1
    COURSE = 2


class ModelFormFactory:
    @staticmethod
    def create_model_form(model_form_type, request, entity_from_db):

        if request is None:
            return ModelFormFactory.__create_model_form_by_values(model_form_type, entity_from_db)

        elif model_form_type is ModelFormType.USER_CREATE:
            return UserCreateForm(request, instance=entity_from_db)

        elif model_form_type is ModelFormType.USER_UPDATE:
            return UserUpdateForm(request, instance=entity_from_db)

        elif model_form_type is ModelFormType.COURSE:
            return CourseForm(request, instance=entity_from_db)

        else:
            return None

    @staticmethod
    def __create_model_form_by_values(model_form_type, record):

        if model_form_type is ModelFormType.USER_CREATE:
            return UserCreateForm(instance=record)

        if model_form_type is ModelFormType.USER_UPDATE:
            return UserUpdateForm(instance=record)

        elif model_form_type is ModelFormType.COURSE:
            return CourseForm(instance=record)

        else:
            return None
