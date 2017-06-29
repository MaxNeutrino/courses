from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    def select_where(column_name, table_name, where_expression):
        return "SELECT {} FROM {} WHERE {}".format(column_name, table_name, where_expression)

    def select_all(self, column_name, table_name):
        return "SELECT {} FROM {}".format(column_name, table_name)

    def delete_where(self, column_name, table_name, where_expression):
        return "DELETE {} FROM {} WHERE {}".format(column_name, table_name, where_expression)

    '''
    Use fields and values how string
    '''

    def insert(self, table_name, fields, values):
        return "INSERT INTO {} ({}) VALUES ({})".format(table_name, fields, values)

    @abstractmethod
    def update(self):
        pass


class UserRepository(AbstractRepository):
    all_columns = "*"
    table_name = "users"

    def find_by_id(self, id):
        query = self.select_where(self.all_columns, self.table_name, "id = " + id)

    def find_all(self):
        query = self.select_all(self.all_columns, self.table_name)

    def remove_by_id(self, id):
        query = self.delete_where(self.all_columns, self.table_name, "id = " + id)

    def save(self, user):
        query = self.insert(
            self.table_name,
            "name,email,phone,mobile_phone,status",
            "{},{},{},{},{}".format(user.name, user.email, user.phone, user.mobile_phone, user.status)
        )

    def update(self, user):
        query = "UPDATE " + self.table_name + " SET " + \
                "name = " + user.name + \
                ", email = " + user.email + \
                ", phone = " + user.phone + \
                ", mobile_phone = " + user.mobile_phone + \
                ", status = " + user.status + \
                " WHERE id = " + user.id


class CourseRepository(AbstractRepository):
    all_columns = "*"
    table_name = "courses"

    def find_by_id(self, id):
        query = self.select_where(self.all_columns, self.table_name, "id = " + id)

    def find_all(self):
        query = self.select_all(self.all_columns, self.table_name)

    def remove_by_id(self, id):
        query = self.delete_where(self.all_columns, self.table_name, "id = " + id)

    def save(self, course):
        query = self.insert(
            self.table_name,
            "name,code",
            "{},{}".format(course.name, course.code)
        )

    def update(self, course):
        query = "UPDATE " + self.table_name + " SET " + \
                "name = " + course.name + \
                ", code = " + course.code + \
                " WHERE id = " + course.id
