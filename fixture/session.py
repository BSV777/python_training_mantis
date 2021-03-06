from selenium.webdriver.common.by import By
from time import sleep

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def ensure_login(self, username, password):
        wd = self.app.wd
        # if self.is_logged_in_as(username):
        #     return
        # else:
        #     self.logout()
        self.login(username, password)

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "username").send_keys(username)
        #wd.find_element(By.ID, "username").send_keys(username)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()
        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "logout_page.php")

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        self.app.open_home_page()
        return wd.find_elements(By.XPATH, "//li/span")[0].text
