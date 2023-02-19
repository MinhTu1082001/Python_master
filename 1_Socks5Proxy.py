from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import requests

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
# browser = webdriver.Firefox(options=options, executable_path="E:\PYTHON\Selenium-Project-master\geckodriver.exe")

# myProxy = "13.55.51.101:8080"

myProxy = "200.106.184.21:999"
ip, port = myProxy.split(":")
fp = webdriver.FirefoxProfile()
fp.set_preference('network.proxy.type', 1)
fp.set_preference('network.proxy.socks', ip)
fp.set_preference('network.proxy.socks_port', int(port))
driver = webdriver.Firefox(firefox_profile=fp, options=options, executable_path="E:\PYTHON\Selenium-Project-master\geckodriver.exe")
# html = requests.get('http://api.ipify.org')
# driver.get('https://whoer.net/')
driver.get('https://api.ipify.org')
sleep(1000)