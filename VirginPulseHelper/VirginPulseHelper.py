from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, InvalidCookieDomainException
from selenium.webdriver.chrome.options import Options
import time
import unittest
import os
import random


class VirginPulseHelper(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=selenium")
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.addCleanup(self.browser.quit)
        self.login()

    def login(self):
        uname = os.environ.get("USERNAME")
        secret = os.environ.get("SECRET")
        # Find form
        self.browser.get("https://app.member.virginpulse.com/")
        try:
            self.browser.find_element_by_xpath('//*[@id="username"]')
        except NoSuchElementException:
            # Prompt user to pass MFA
            input("Captcha detected: Press Enter to continue after passing Captcha")
            pass
        time.sleep(random.choice([1, 2, 4]))
        self.browser.find_element_by_xpath('//*[@id="username"]').send_keys(uname)
        self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(secret)
        time.sleep(random.choice([2, 5, 7]))
        self.browser.find_element_by_xpath('//*[@id="kc-login"]').click()
        time.sleep(random.choice([3, 5, 6]))
        # Check if MFA is needed (i.e. Not taken to home menu)
        try:
            self.browser.find_element_by_xpath('//*[@id="core-menuitem-logo"]')
        except NoSuchElementException:
            # Prompt user to pass MFA
            input("MFA Prompt detected: Press Enter to continue after passing MFA")
            pass

    def clickButton(self, xpath):
        try:
            self.browser.find_element_by_xpath(xpath).click()
            return True
        except NoSuchElementException:
            return False

    def testDoCards(self):
        # Just return for now, working on login
        self.browser.get("https://app.member.virginpulse.com/#/home")
        time.sleep(random.choice([10, 12, 14]))
        # Do cards
        # TODO Need to check if just an okay or True/False card
        self.clickButton('//*[@id="triggerCloseCurtain"]')
        time.sleep(5)
        self.clickButton('//*[@id="triggerCloseCurtain"]')

        # Do habits
        for i in range(1, 19):
            self.clickButton(f"/html/body/div[2]/div/div/div[1]/div/basic-home/div/div[2]/div[3]/home-healthy-habits/div/div/div[{i}]/home-healthy-habit-tile/div/div[4]/button[{random.choice([1, 2])}]")
            time.sleep(random.choice([1, 2, 3]))




if __name__ == '__main__':
    unittest.main()
