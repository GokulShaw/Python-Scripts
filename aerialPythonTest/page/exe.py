from selenium import webdriver
import json

driver = webdriver.Chrome("/Users/d/PycharmProjects/aerialPythonTest/driver/chromedriver")



driver.maximize_window()

driver.get("https://github.com/")

driver.implicitly_wait(10)

driver.find_element_by_xpath("//a[contains(text(),'Sign in')]").click()

with open("/Users/d/PycharmProjects/aerialPythonTest/jsonfiles/egFull.json") as gitName:
    datum = json.load(gitName)
for i in datum['LoginDetails']:
    driver.find_element_by_xpath("//input[@id='login_field']").send_keys(i['userName'])
    driver.find_element_by_id("password").send_keys(i['password'])

driver.find_element_by_xpath("//input[@type='submit']").click()

'''driver.find_element_by_xpath("//summary[@class='Header-link']//img").click()

element = driver.find_element_by_xpath("//a[contains(text(),'Signed')]//strong")
text = element.get_attribute("innerText")
print(text)'''

driver.execute_script("window.scrollBy(0,1000)","")






