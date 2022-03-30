
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started")
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(1)
driver.find_element_by_id("twotabsearchtextbox").send_keys("One plus 9R 5G")
time.sleep(1)
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(60)
driver.close()
print("test case completed")




