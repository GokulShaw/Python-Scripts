from selenium import webdriver

from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="/Users/d/PycharmProjects/aerialPythonTest/driver/chromedriver")

driver.get("https://www.flipkart.com/")

driver.implicitly_wait(10)

driver.maximize_window()

#scroll by specified pixels

#driver.execute_script("window.scrollBy(0, 10000)", " ")

#scroll down till the element is visible

#flag = driver.find_element_by_xpath("//div[text()='India']/parent::*")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

#scroll to the bottom

#driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

#move hover

'''
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()

all = driver.find_element_by_xpath("//div[text()='Electronics']")
time.sleep(2)
mobile = driver.find_element_by_xpath("//a[text()='Mobile']")

act = ActionChains(driver)
act.move_to_element(all).move_to_element(mobile).click().perform()

#capture all the cookies in created by browser

cookies = driver.get_cookies()
print(len(cookies))

#print all the cookies there

print(cookies)

#Adding new cookie to the browser

cookie = {
    'name':'MyCokkie', 'value':'12356486'
}
driver.add_cookie(cookie)


cookies = driver.get_cookies()
print(len(cookies))

#deletimg the name of the cookie

driver.delete_cookie('MyCokkie')
cookies = driver.get_cookies()
print(len(cookies))
'''






