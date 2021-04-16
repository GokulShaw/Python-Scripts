
import time
class HomePageAerial():

    def __init__(self, driver):
        self.driver = driver
        self.popupClickAerial = "//div[text()='Got it']"
        self.demographicsClick = "//div[@id='appEnrollment_menu']"

    def clickGotit(self):
        self.driver.find_element_by_xpath(self.popupClickAerial).click()

    def Demographics(self):
        self.driver.find_element_by_xpath(self.demographicsClick).click()
        time.sleep(5)
