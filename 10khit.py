import time
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests


weblink = 'https://www.10khits.com/login'

firefox_options = Options()
firefox_options.add_argument("start-maximized")
firefox_options.add_argument("-private")
# firefox_options.add_argument("--headless")
driver = webdriver.Firefox(options=firefox_options)

driver.set_window_size(1920, 1080)
driver.get(weblink)

print("* Loaded "+weblink+" *")
print("----------------------")

time.sleep(1)
input_email = driver.find_element(By.ID, 'email')
time.sleep(1)
input_email.send_keys("long.nguyen2198@gmail.com")

input_password = driver.find_element(By.ID, 'password')
time.sleep(1)
input_password.send_keys("Rongnhat2a@")


time.sleep(1)
driver.execute_script("document.getElementsByTagName('button')[0].click()")


time.sleep(20)
driver.quit() 