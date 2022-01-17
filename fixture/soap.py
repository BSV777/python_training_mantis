from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        project_list = []
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        mc_projects = client.service.mc_projects_get_user_accessible(
            self.app.config['webadmin']['username'], self.app.config['webadmin']['password'])

        for project in mc_projects:
             project_list.append(Project(id=project.id, name=project.name, status=project.status.name,
                                 view_state=project.view_state.name, description=project.description))
        return project_list
