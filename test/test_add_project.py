from time import sleep
from model.project import Project
import datetime


def test_add_project(app, db):
    #old_projects = db.get_project_list()
    old_projects = app.soap.get_project_list()

    project = Project(id=None, name="Proj_" + datetime.datetime.today().strftime("%Y%m%d_%H%M%S"),
                            status="release", inherit=True, view_state="private", description="Test project")

    app.project.add_project(project)
    # new_projects = db.get_project_list()
    new_projects = app.soap.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


