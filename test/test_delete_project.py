from model.project import Project
import datetime
import random


def test_delete_project(app, db):
    if len(db.get_project_list()) == 0:
        project = Project(id=None, name="Proj_" + datetime.datetime.today().strftime("%Y%m%d_%H%M%S"),
                          status="release", inherit=True, view_state="private", description="Test project")
        app.project.create(project)
    old_projects = db.get_project_list()

    app.session.login("administrator", "root")
    app.project.open_projects_page()

    #app.project.delete_project_by_name("Proj_20220114_165232")
    #app.project.delete_project_by_id("4")

    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)

    new_projects = db.get_project_list()

    old_projects.remove(project)

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

    app.session.logout()