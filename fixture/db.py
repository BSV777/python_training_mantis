import pymysql.cursors
from model.project import Project


class DBFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_project_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, status, view_state, inherit_global, description from mantis_project_table")
            for row in cursor:
                (id, name, status, view_state, inherit, description) = row
                list.append(Project(id=str(id), name=name, status=status, view_state=view_state,
                                    inherit=inherit, description=description))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

