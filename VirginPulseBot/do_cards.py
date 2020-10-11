from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

browser.get("https://app.member.virginpulse.com/")


def login(webdriver):
    webdriver.find_element_by_id('oUserID').send_keys()
    webdriver.find_element_by_id('oPwdID').send_keys()
    time.sleep(1)
