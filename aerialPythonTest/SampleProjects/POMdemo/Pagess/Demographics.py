from selenium.webdriver import ActionChains
import time
class DemographicsAerial():
    def __init__(self, driver):
        self.driver = driver
        self.getPatientId = "//input[@name='PatientId']"
        self.searchButton = "//div[@eventproxy='Search']//td"
        self.DoubleClick = "//tr[@role='listitem']"



    def PatientId(self, id):
        a = self.driver.find_element_by_xpath(self.getPatientId)
        a.click()
        a.send_keys(id)

    def SearchPatient(self):
        b = self.driver.find_element_by_xpath(self.searchButton)
        b.click()
        time.sleep(3)

    def ClickDouble(self):
        source = self.driver.find_element_by_xpath(self.DoubleClick)
        action = ActionChains(self.driver)
        action.double_click(source).perform()
        time.sleep(3)