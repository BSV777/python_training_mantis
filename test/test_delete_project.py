from model.project import Project
import datetime
import random


def test_delete_project(app, db):
    if len(db.get_project_list()) == 0:
        project = Project(id=None, name="Proj_" + datetime.datetime.today().strftime("%Y%m%d_%H%M%S"),
                          status="release", inherit=True, view_state="private", description="Test project")
        app.project.create(project)
    # old_projects = db.get_project_list()
    old_projects = app.soap.get_project_list()

    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)

    # new_projects = db.get_project_list()
    new_projects = app.soap.get_project_list()

    old_projects.remove(project)

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

