from selenium import webdriver
#from time import sleep
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import time
import json

driver = webdriver.Chrome(executable_path="../driver/chromedriver")
driver.get("https://qa.gsihealth.net/")
driver.implicitly_wait(10)

with open('/Users/d/PycharmProjects/aerialPythonTest/jsonfiles/egFull.json') as file:
    data = json.load(file)
for loot in data['LoginDetails']:
    driver.find_element_by_xpath("//input[@id='login-username']").send_keys(loot['userName'])
    driver.find_element_by_xpath("//input[@id='login-password']").send_keys(loot['password'])

driver.find_element_by_xpath("//input[@id='login-username']/following::button").click()

element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Got it']"))
)
element.click()

#driver.find_element_by_xpath("//div[text()='Got it']").click()

#driver.find_element_by_xpath("//div[@class='q-btn-group row no-wrap inline q-btn-group-push']/child::button[1]").click()

driver.find_element_by_xpath("//div[@id='appEnrollment_menu']").click()

#a = WebDriverWait(driver, 10).until(
  #  EC.presence_of_element_located((By.XPATH, "//*[@id='isc_22']"))
#)
#a.click()
#a.send_keys("1313")

time.sleep(10)
a = driver.find_element_by_xpath("//*[@id='isc_22']")
a.click()
a.send_keys("1313")

b = driver.find_element_by_xpath("//*[@id='isc_I']/table/tbody/tr/td")
b.click()

time.sleep(5)
source = driver.find_element_by_xpath("//*[@id='isc_50']/div")
action = ActionChains(driver)
action.double_click(source).perform()

time.sleep(3)
driver.find_element_by_xpath("//div[text()='Modify']").click()

time.sleep(3)

driver.find_element_by_xpath("//input[@name='streetAddress1']").clear()
driver.find_element_by_xpath("//input[@name='streetAddress1']").send_keys("New York main road")

time.sleep(3)
driver.find_element_by_xpath("//input[@name='newTextItem_3']").clear()
driver.find_element_by_xpath("//input[@name='newTextItem_3']").send_keys("Atlantas")


'''swc = driver.find_element_by_xpath("//*[@id='isc_HC']")
dropdown = Select(swc)
dropdown.select_by_visible_text("GA")
#dropdown.select_by_index(10)'''
'''
wait1 = WebDriverWait(driver,10)
element1 = wait1.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='isc_HC']")))
element1.click()

time.sleep(3)
drop = driver.find_element_by_xpath("//div[@id='isc_MU']//div[text()='GA']")
drop.click()

wait2 = WebDriverWait(driver,10)
element2 = wait2.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='isc_MU']//div[text()='GA']")))
element2.click()
'''

driver.find_element_by_xpath("//img[@id='isc_HF']").click()
time.sleep(1.5)
driver.find_element_by_xpath("//div[contains(@class,'pickListMenuBody')]//following::div[contains(text(),'GA')]").click()

zipcode = driver.find_element_by_xpath("//td[contains(text(),'Information')]//preceding::input[@name='newTextItem_12']")
zipcode.click()
time.sleep(3)
zipcode.send_keys("88888")

#driver.find_element_by_xpath("//td[contains(text(),'Information')]//preceding::input[@name='newTextItem_12']").send_keys("89654")
driver.find_element_by_xpath("//div[contains(@eventproxy,'SaveButton')]//div[contains(text(),'Save')]").click()

time.sleep(3)
driver.find_element_by_xpath("//div[contains(@class,'windowBackground')]//following::div[@role='toolbar']/child::div/child::div").click()

driver.find_element_by_xpath("//button[@type='button']//following::span[contains(text(),'Reset')]").click()