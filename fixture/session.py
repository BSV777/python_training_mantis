from selenium.webdriver.common.by import By
#from time import sleep

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "username").send_keys(username)
        #wd.find_element(By.ID, "username").send_keys(username)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()
        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        self.app.logout()

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, "span.label.hidden-xs.label-default.arrowed").text
