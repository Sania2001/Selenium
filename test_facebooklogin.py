import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started")
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(1)
driver.find_element_by_name("email").send_keys("Sania")
driver.find_element_by_name("pass").send_keys("Shinde")
time.sleep(1)
driver.find_element_by_name("login").click()
time.sleep(6)
driver.close()
print("test case completed")