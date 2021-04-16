class LoginPageAerial():

    def __init__(self, driver):
        self.driver = driver

        self.username_aerial = "//input[@id='login-username']"
        self.password_aerial = "//input[@id='login-password']"
        self.login_button_aerial = "//input[@id='login-username']/following::button"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_aerial).clear()
        self.driver.find_element_by_xpath(self.username_aerial).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_aerial).clear()
        self.driver.find_element_by_xpath(self.password_aerial).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_aerial).click()