from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "username").send_keys(username)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()
        wd.find_element(By.NAME, "Password").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='submit']").click()

    def logout(self):
        wd = self.app.wd
        #wd.get(self.base_url + "logout_page.php")
        self.app.logout()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        # return wd.find_element(By.XPATH, "//div/div[1]/form/b").text == "(%s)" % username
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        # return wd.find_element(By.XPATH, "//div/div[1]/form/b").text[1:-1]
        return "administrator"

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)