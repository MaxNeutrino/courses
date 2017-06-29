import logging

from service.repository import UserRepository, CourseRepository


class UserService:
    logger = logging.getLogger("UserService")
    repository = UserRepository()

    def find(self, user_id):
        self.logger.debug("find user_id = %d", user_id)
        return self.repository.find(user_id)

    def find_all(self):
        self.logger.debug("find_all")
        return self.repository.find_all()

    def remove(self, user_id):
        self.logger.debug("remove id = %d", user_id)
        self.repository.remove(user_id)

    def save(self, user):
        self.logger.debug("save user = %s", user.__str__())
        self.repository.save(user)

    def update(self, user):
        self.logger.debug("update user = %s", user.__str__())
        self.repository.update(user)


class CourseService:
    logger = logging.getLogger("CourseService")
    repository = CourseRepository()

    def find(self, course_id):
        self.logger.debug("find user_id = %d", course_id)
        return self.repository.find(course_id)

    def find_all(self):
        self.logger.debug('find_all')
        return self.repository.find_all()

    def find_by_user_id(self, user_id):
        self.logger.debug('find_by_user_id = %d', user_id)
        return self.repository.find_by_user_id(user_id)

    def remove(self, course_id):
        self.logger.debug('remove id = %d', course_id)
        self.repository.remove(course_id)

    def save(self, course):
        self.logger.debug('save course = %s', course.__str__())
        self.repository.save(course)

    def update(self, course):
        self.logger.debug('update course = %s', course.__str__())
        self.repository.update(course)
