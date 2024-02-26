import time
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests


weblink = 'https://coinmarketcap.com/currencies/microvisionchain/'

firefox_options = Options()
firefox_options.add_argument("start-maximized")
# firefox_options.add_argument("-private")
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(options=firefox_options)

driver.set_window_size(1920, 1080)
driver.get(weblink)

print("* Loaded "+weblink+" *")
print("----------------------")

listLink = []
main = driver.find_element(By.CLASS_NAME, "coin-stats")
link = main.find_elements(By.XPATH, './/descendant::a[@href]')
for i in link:
	if "mailto:" in i.get_attribute('href'):
		mail = i.get_attribute('href').split(":")[1].lower()
		if mail not in listLink:
			listLink.append(mail)

	if "twitter." in i.get_attribute('href'):
		twitter = i.get_attribute('href').split("?")[0].lower()
		if twitter not in listLink:
			listLink.append(twitter)

	if "linkedin." in i.get_attribute('href'):
		linkedin = i.get_attribute('href').split("?")[0].lower()
		if linkedin not in listLink:
			listLink.append(linkedin)

	if "instagram." in i.get_attribute('href'):
		instagram = i.get_attribute('href').split("?")[0].lower()
		if instagram not in listLink:
			listLink.append(instagram)

	if "youtube." in i.get_attribute('href'):
		youtube = i.get_attribute('href').split("?")[0].lower()
		if youtube not in listLink:
			listLink.append(youtube)

	if "spotify." in i.get_attribute('href'):
		spotify = i.get_attribute('href').split("?")[0].lower()
		if spotify not in listLink:
			listLink.append(spotify)

	if "mirror." in i.get_attribute('href'):
		mirror = i.get_attribute('href').split("?")[0].lower()
		if mirror not in listLink:
			listLink.append(mirror)

	if "github." in i.get_attribute('href'):
		github = i.get_attribute('href').split("?")[0].lower()
		if github not in listLink:
			listLink.append(github)

	if "telegram." in i.get_attribute('href'):
		telegram = i.get_attribute('href').split("?")[0].lower()
		if telegram not in listLink:
			listLink.append(telegram)

	if "t.me" in i.get_attribute('href'):
		telegram = i.get_attribute('href').split("?")[0].lower()
		if telegram not in listLink:
			listLink.append(telegram)

	if "discord." in i.get_attribute('href'):
		discord = i.get_attribute('href').split("?")[0].lower()
		if discord not in listLink:
			listLink.append(discord)

	if "reddit." in i.get_attribute('href'):
		reddit = i.get_attribute('href').split("?")[0].lower()
		if reddit not in listLink:
			listLink.append(reddit)

	if "www." in i.get_attribute('href'):
		www = i.get_attribute('href').split("?")[0].lower()
		if www not in listLink:
			listLink.append(www)


for x in listLink:
	print(x)
	
print("----------------------")
print("* Finished *") 
driver.quit() 