import pymysql.cursors

from tz.models import User, Course


def user_map(row):
    user = User()
    user.id = row['id']
    user.name = row['name']
    user.email = row['email']
    user.phone = row['phone']
    user.mobile_phone = row['mobile_phone']
    user.status = bool(row['status'])
    return user


def course_map(row):
    course = Course()
    course.id = row['id']
    course.name = row['name']
    course.code = row['code']
    return course


def execute_and_commit(connection, query):
    if connection is not None:
        with connection.cursor() as cursor:
            cursor.execute(query)
        connection.commit()


class DbConnectorHandler(object):
    __instance = None
    connection = None

    @staticmethod
    def instance():
        if DbConnectorHandler.__instance is None:
            DbConnectorHandler.__instance = DbConnectorHandler()
            DbConnectorHandler.__instance.init_db()
        return DbConnectorHandler.__instance

    def init_db(self):
        if self.connection is not None:
            self.close()

        self.connection = pymysql.connect(host='localhost', user='user', password='user', db='users',
                                          charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    def close(self):
        self.connection.close()


class UserRepository:
    connection = DbConnectorHandler.instance().connection

    def find(self, user_id):
        query = "SELECT * FROM users WHERE id={}".format(user_id)

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()
            user = user_map(row)

        return user

    def find_all(self):
        query = "SELECT * FROM users"
        users = []

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                user = user_map(row)
                users.append(user)

        return users

    def remove(self, user_id):
        query = "DELETE FROM users WHERE id={}".format(user_id)
        execute_and_commit(self.connection, query)

    def save(self, user):
        query = "INSERT INTO users (name,email,phone,mobile_phone,status) " + \
                "VALUES(\'{}\',\'{}\',\'{}\',\'{}\',{})".format(
                    user.name, user.email, user.phone, user.mobile_phone, bool(user.status))

        execute_and_commit(self.connection, query)

    def update(self, user):
        query = ("UPDATE users SET " +
                 "name=\'{0}\', " +
                 "email=\'{1}\', " +
                 "phone=\'{2}\', " +
                 "mobile_phone=\'{3}\', " +
                 "status={4} " +
                 "WHERE id={5}").format(
            user.name, user.email, user.phone, user.mobile_phone, bool(user.status), user.id
        )

        execute_and_commit(self.connection, query)


class CourseRepository:
    connection = DbConnectorHandler.instance().connection

    def find(self, course_id):
        query = "SELECT * FROM courses WHERE id={}".format(course_id)
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()
            course = course_map(row)
        return course

    def find_all(self):
        query = "SELECT * FROM courses"
        courses = []
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                course = course_map(row)
                courses.append(course)

        return courses

    def find_by_user_id(self, user_id):
        query = "SELECT * FROM user_courses WHERE user_id={}".format(user_id)
        user_courses = []

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                course_id = row['course_id']
                course = self.find(course_id)
                user_courses.append(course)

        return user_courses

    def remove(self, course_id):
        query = "DELETE FROM courses WHERE id={}".format(course_id)
        execute_and_commit(self.connection, query)

    def save(self, course):
        query = "INSERT INTO courses (name,code) " + \
                "VALUES({},{})".format(
                    course.name, course.code)
        execute_and_commit(self.connection, query)

    def update(self, course):
        query = ("UPDATE courses SET " +
                 "name=\'{0}\', " +
                 "code=\'{1}\' " +
                 "WHERE id={2}").format(course.name, course.code, course.id)
        execute_and_commit(self.connection, query)
