from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path="../driver/chromedriver")
driver.get("https://qa.gsihealth.net/")
driver.find_element_by_xpath("//input[@id='login-username']").send_keys("usertesttraining@test.com")
driver.find_element_by_xpath("//input[@id='login-password']").send_keys("Test123#")
driver.find_element_by_xpath("//input[@id='login-username']/following::button").click()