from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_path = "C:/Users/nrani/Downloads/chromedriver.exe"
service = Service(driver_path)
browser = webdriver.Chrome(service=service)
browser.get("https://www.wikipedia.org/")
time.sleep(2)
browser.maximize_window()
ele1 = browser.find_element(By.XPATH, "//a[@title='English — Wikipedia — The Free Encyclopedia']")
ele1.click()
time.sleep(3)
ele2 = browser.find_element(By.XPATH, "//input[@type='search']")
ele2.click()
time.sleep(2)
ele2.click()
time.sleep(2)
ele2.send_keys("Selenium (software)")
time.sleep(2)
ele3 = browser.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div/div/div/div/form/div/button")
ele3.click()
time.sleep(2)
browser.execute_script("window.scrollBy(0, 500);")
time.sleep(2)
browser.execute_script("window.scrollBy(0, 500);")
time.sleep(2)
browser.quit()