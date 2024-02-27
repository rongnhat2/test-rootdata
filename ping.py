import time
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
import json 
import requests


weblink = 'https://www.rootdata.com/Projects/detail/OX.FUN?k=MTEyMzU%3D'

firefox_options = Options()
firefox_options.add_argument("start-maximized")
# firefox_options.add_argument("-private")
firefox_options.add_argument("--headless")

driver = webdriver.Firefox(options=firefox_options)

driver.set_window_size(1920, 1080)
driver.get(weblink)
print(weblink)
try:
    driver.execute_script("document.getElementsByClassName('tracker_wrap')[1].click()")
    time.sleep(5)
    driver.back()
    time.sleep(5)

    for request in driver.requests:
        if request.method == 'POST' and "item_detail" in request.url:
            payload_data = request.body.decode('UTF-8')
            print(payload_data)
except Exception as e:
    print(e)
    print("* Project Link *")

print("----------------------")
print("* Finished *")
driver.quit() 