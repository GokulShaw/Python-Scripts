from selenium import webdriver

import unittest

from SampleProjects.POMdemo.Pagess.LoginPage import LoginPageAerial
from SampleProjects.POMdemo.Pagess.HomePage import HomePageAerial
from SampleProjects.POMdemo.Pagess.Demographics import DemographicsAerial
from SampleProjects.POMdemo.Pagess.ModifyPage import ModifyAerial
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
import HtmlTestRunner

class LoginTestPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/d/PycharmProjects/aerialPythonTest/driver/chromedriver")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        print("Chrome Driver Started")

    def test_login_page(self):
        driver = self.driver

        driver.get("https://qa.gsihealth.net/")

        #loginPage
        login = LoginPageAerial(driver)


        wait = WebDriverWait(driver, 5)
        emil = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Let')]")))
        if emil.text == "Let's make things better!":
            print("Login page Started Successfully")
        else:
            print("Login Page Failed to Run    ")


        with open('/Users/d/PycharmProjects/aerialPythonTest/jsonfiles/login.json') as fle:
            data = json.load(fle)
        for loot in data['LoginDetails']:
            login.enter_username(loot['userName'])
            login.enter_password(loot['password'])

        login.click_login()

        #homePage
        ele = driver.find_element_by_xpath("//span[contains(text(),'UserTest')]")
        if ele.text == 'UserTest Test':
            print("Valid User is Logged in")
        else:
            print("User verification Failed, UserName should be : ", + ele.text)

        home = HomePageAerial(driver)

        wait1 = WebDriverWait(driver, 3)
        emil1 = wait1.until(EC.visibility_of_element_located((By.XPATH,"//span[@id='home-toolbar']/following::span[1]")))
        if emil1.text == "SUMMARY DASHBOARD":
            print("Home Page Started Successfully")
        else:
            print("Home Page Failed to Run")

        home.clickGotit()
        home.Demographics()

        #demographics

        ele1 = driver.find_element_by_xpath("//label//font[contains(text(),'Search all')]")
        if ele1.text == 'Search all patients':
            print("     Demographics tab is clicked")
        else:
            print("     Demographics tab is not clicked ", + ele1.text)


        demo = DemographicsAerial(driver)

        wait2 = WebDriverWait(driver, 3)
        emil2 = wait2.until(EC.visibility_of_element_located((By.XPATH,"//td[@class='sectionHeaderopened']//child::div")))
        if emil2.text == "Demographics":
            print("DemoGraphics page Started Successfully")
        else:
            print("DemoGraphics page Failed to Run")

        demo.PatientId("1313")
        demo.SearchPatient()

        ele2 = driver.find_element_by_xpath("//div[contains(text(),'1313')]")
        if ele2.text == '1313':
            print("     Patient Id entered is correct")
        else:
            print("     Patient Id entered is incorrect")

        demo.ClickDouble()



        #modify
        ele3 = driver.find_element_by_xpath("//td[contains(text(),'View')]")
        if ele3.text == 'View Patient':
            print("     Double click is Done to Navigate to Modification Page")
        else:
            print("     Double Click Action Failed")


        modify = ModifyAerial(driver)

        wait3 = WebDriverWait(driver, 5)
        emil3 = wait3.until(EC.visibility_of_element_located((By.XPATH,"//td[contains(text(),'View')]")))
        if emil3.text == "View Patient":
            print("Modification  page Started Successfully")
        else:
            print("Modification page Failed to Run")


        modify.ModifyClick()

        ele4 = driver.find_element_by_xpath("//td[contains(text(),'Modify')]")
        if ele4.text == 'Modify Patient':
            print("     Modify Button is clicked to Navigate to the Modification Page")
        else:
            print("     Modify Click Button Action Failed")


        modify.AddressName1("NewYork")
        modify.CityName1("Los Angels")
        modify.ButtonDropDown()
        modify.StateDropDown()
        modify.ZipCodeItem("85846")
        modify.SaveClick()
        modify.OkWindow()

        '''ele5 = driver.find_element_by_xpath("//div[contains(text(),'NewYork')]")
        if ele5.text == 'NewYork':
            print("Address1 name is Successfully Verified")
        else:
            print("Address1 name is incorrect")

        ele6 = driver.find_element_by_xpath("//div[contains(text(),'Los')]")
        if ele6.text == 'Los Angels':
            print("Changes in City name is Successfully Verified")
        else:
            print("City name is incorrect")

        ele7 = driver.find_element_by_xpath("//div[contains(text(),'GA')]")
        if ele7.text == 'GA':
            print("Changes in State is Successfully Verified from the dropdown")
        else:
            print("State verification Failed")

        ele8 = driver.find_element_by_xpath("//div[contains(text(),'NewYork')]")
        if ele8.text == 'NewYork':
            print("Address1 name is Successfully Verified")
        else:
            print("Address1 name is incorrect")'''


        modify.ResetClick()


    @classmethod
    def tearDownClass(cls):
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/d/PycharmProjects/aerialPythonTest/SampleProjects/POMdemo/reports"))