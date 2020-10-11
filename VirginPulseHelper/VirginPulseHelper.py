from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
import os
import random


class VirginPulseHelper(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        self.login()

    def login(self):
        # Find form
        self.browser.get("https://app.member.virginpulse.com/")
        uname = os.environ.get("USERNAME")
        secret = os.environ.get("SECRET")
        self.browser.find_element_by_xpath('//*[@id="username"]').send_keys(uname)
        self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(secret)
        time.sleep(random.choice([1, 2, 3]))
        self.browser.find_element_by_xpath('//*[@id="kc-login"]').click()
        time.sleep(random.choice([1, 2, 3]))

    def clickButton(self, xpath):
        try:
            self.browser.find_element_by_xpath(xpath).click()
            return True
        except NoSuchElementException:
            return False

    def testDoCards(self):
        self.browser.get("https://app.member.virginpulse.com/#/home")
        if not self.clickButton('//*[@id="triggerCloseCurtain"]'):
            return False
        time.sleep(5)
        if not self.clickButton('//*[@id="triggerCloseCurtain"]'):
            return False
        return True

    def testDoHealthyHabits(self):
        self.browser.get("https://app.member.virginpulse.com/#/home")
        for i in range(1, 19):
            self.clickButton(f"/html/body/div[2]/div/div/div[1]/div/basic-home/div/div[2]/div[3]/home-healthy-habits/div/div/div[{i}]/home-healthy-habit-tile/div/div[4]/button[{random.choice([1, 2])}]")
            time.sleep(random.choice([1, 2, 3]))




if __name__ == '__main__':
    unittest.main()
