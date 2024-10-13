#This code will create a bot to choose an instagram account and have an attempt on following his followers.
#It's basically an instagram BOT.

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException

Similar_Account='xxxxxxxx'
Username='xxxxxxxxxxxx'
Password='xxxxxxxxxx'

class InstaFollowers:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)



    def login(self):
        self.driver.get(url='https://www.instagram.com')
        time.sleep(1)
        username=self.driver.find_element(By.NAME, value="username")
        username.send_keys(Username)
        password = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.NAME, "password")))
        time.sleep(1)
        password.send_keys(Password,Keys.ENTER)
        time.sleep(5)
        login_save = self.driver.find_element(By.XPATH, '//div[text()="Not now"]')
        login_save.click()
        time.sleep(3)
        Turn_on_notifications=self.driver.find_element(By.XPATH, value="//button[normalize-space()='Not Now']")
        Turn_on_notifications.click()

    def find_followers(self):
        time.sleep(3)
        self.driver.get(url='https://www.instagram.com/chefsteps/')
        time.sleep(3)
        followers=self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a')
        followers.click()
        time.sleep(5)
        modal = self.driver.find_element(By.XPATH, value="/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        #The script below will use the bar element to increase the number of followers by tapping 5 times on the bar and expanding the list.
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        followers=self.driver.find_element(By.XPATH, value= '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div')
        follower = followers.find_elements(By.TAG_NAME,'button')

        for each_follower in follower:
            try:
                each_follower.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, value='//button[contains(text(), "Aceptar")]')
                cancel.click()
                time.sleep(2)

insta=InstaFollowers()
insta.login()
insta.find_followers()
insta.follow()
