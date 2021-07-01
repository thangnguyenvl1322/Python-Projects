from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
Path = ('C:/Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(executable_path=Path,options=chrome_options)
driver.get('https://www.google.com/')

searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')

time.sleep(2)

searchbox.send_keys('running')
searchbox.send_keys(Keys.RETURN)
