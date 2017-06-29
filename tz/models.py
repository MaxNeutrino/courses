class Course:
    id = None
    name = None
    code = None

    def __str__(self):
        return "id = {}, name = {}, code = {}".format(
            self.id, self.name, self.code
        )


class User:
    id = None
    name = None
    email = None
    phone = None
    mobile_phone = None
    status = None
    courses = None

    def __str__(self):
        return "id = {}, name = {}, email = {}, phone = {}, mobile_phone = {}, status = {}".format(
            self.id, self.name, self.email, self.phone, self.mobile_phone, self.status
        )


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
