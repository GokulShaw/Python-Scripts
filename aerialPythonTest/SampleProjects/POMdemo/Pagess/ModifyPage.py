import time
class ModifyAerial():
    def __init__(self, driver):
        self.driver = driver
        self.clickModify = "//div[text()='Modify']"
        self.AddressName = "//input[@name='streetAddress1']"
        self.CityName = "//input[@name='newTextItem_3']"
        self.DropDownButton = "//td[@class='comboBoxItemPickerCell']//following::span[@id='isc_HC']/child::*"
        self.StateName = "//div[contains(@class,'pickListMenuBody')]//following::div[contains(text(),'GA')]"
        self.ZipCode = "//td[contains(text(),'Information')]//preceding::input[@name='newTextItem_12']"
        self.SaveButton = "//div[contains(@eventproxy,'SaveButton')]//div[contains(text(),'Save')]"
        self.OkButton = "//div[contains(@role,'toolbar')]/child::*/child::*"
        self.ResetButton = "//button[@type='button']//following::span[contains(text(),'Reset')]"


    def ModifyClick(self):
        self.driver.find_element_by_xpath(self.clickModify).click()
        time.sleep(3)

    def AddressName1(self, address):
        self.driver.find_element_by_xpath(self.AddressName).clear()
        self.driver.find_element_by_xpath(self.AddressName).send_keys(address)
        time.sleep(3)

    def CityName1(self, city):
        self.driver.find_element_by_xpath(self.CityName).clear()
        self.driver.find_element_by_xpath(self.CityName).send_keys(city)
        time.sleep(3)

    def ButtonDropDown(self):
        self.driver.find_element_by_xpath(self.DropDownButton).click()
        time.sleep(3)

    def StateDropDown(self):
        self.driver.find_element_by_xpath(self.StateName).click()
        time.sleep(3)

    def ZipCodeItem(self, ie):
        zipcode = self.driver.find_element_by_xpath(self.ZipCode)
        zipcode.click()
        time.sleep(3)
        zipcode.send_keys("88548")

    def SaveClick(self):
        self.driver.find_element_by_xpath(self.SaveButton).click()
        time.sleep(3)

    def OkWindow(self):
        self.driver.find_element_by_xpath(self.OkButton).click()
        time.sleep(3)

    def ResetClick(self):
        self.driver.find_element_by_xpath(self.ResetButton).click()
        time.sleep(3)

