import time
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
import json 
import requests

i = 0
while i < 20:
	url = "https://launch.rhass.vn/api/get-item"
	response = requests.get(url)
	response.encoding = 'utf-8'  
	print("----------------")
	print("* Loading page *")
	x = json.loads(response.text)

	print(x['name'])
	# weblink = 'https://www.rootdata.com/Projects/detail/'+str(x["name"])+'?k='+str(x["project_decode"])
	# weblink = 'https://www.rootdata.com/Investors/detail/'+str(x["name"])+'?k='+str(x["project_decode"])
	weblink = 'https://www.rootdata.com/member/'+str(x["name"])+'?k='+str(x["project_decode"])

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
		time.sleep(10)
		driver.back()
		time.sleep(10)

		for request in driver.requests:
			# if request.method == 'POST' and "item_detail" in request.url:
			# if request.method == 'POST' and "org_detail" in request.url:
			if request.method == 'POST' and "mem_detail" in request.url:
				payload_data = request.body.decode('UTF-8')
				url = "https://launch.rhass.vn/api/itemInvestor?id="+str(x["id"])+"&payload="+str(payload_data)
				requests.get(url)
	except Exception as e:
		print(e)
		url = "https://launch.rhass.vn/api/itemProject?id="+str(x["id"])
		requests.get(url)
		print("* Project Link *")
	
	time.sleep(5)

	print("----------------------")
	print("* Finished *")
	driver.quit() 