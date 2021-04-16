from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="/Users/d/PycharmProjects/aerialPythonTest/driver/chromedriver")

driver.implicitly_wait(10)

driver.get("https://www.w3schools.com/python/python_dictionaries.asp")

driver.save_screenshot("/Users/d/Documents/workspace2/screenshot/screen.jpg")

time.sleep(3)

driver.get_screenshot_as_file("/Users/d/Documents/workspace2/screenshot/scr.png")