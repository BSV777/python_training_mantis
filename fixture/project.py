from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        self.app.open_projects_page()
        # wd = self.app.wd
        # wd.find_element(By.XPATH, "//a[contains(text(),'Manage Projects')]").click()

    def add_project(self, project):
        wd = self.app.wd
        #wd.find_element(By.LINK_TEXT, "Create New Project").click()
        wd.find_element(By.XPATH, "//button[@type='submit']").click()

        #self.change_field_value("//input[@id='project-name']", name)

        self.change_field_value("name", project.name)
        self.change_option_value("status", project.status)
        self.change_option_value("view_state", project.view_state)
        self.change_field_value("description", project.description)
        wd.find_element(By.XPATH, "//input[@value='Add Project']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def change_option_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(text)

    def delete_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//a[contains(text(),'%s')]" % name).click()
        wd.find_element(By.XPATH, "//input[@value='Delete Project']").click()
        wd.find_element(By.XPATH, "//input[@type='submit']").click()

    def delete_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % id).click()
        wd.find_element(By.XPATH, "//input[@value='Delete Project']").click()
        wd.find_element(By.XPATH, "//input[@type='submit']").click()
