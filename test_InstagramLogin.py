from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
username = input("Enter username")
password = input("Enter password")
print("Test case started")
driver.maximize_window()
driver.get("https://www.instagram.com/")
time.sleep(1)
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(60)
driver.close()
print("test case completed")