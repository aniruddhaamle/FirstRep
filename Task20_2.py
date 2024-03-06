import os
import urllib
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Labour:
    """
    This class is used to work on https://labour.gov.in/
    """

    def __init__(self, url="https://labour.gov.in/", username="standard_user", password="secret_sauce"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
        This method is used to open the browser and go to https://labour.gov.in/ .
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(3)

    def findElementByXP(self, value):
        return self.driver.find_element(by=By.XPATH, value=value)

    def download_MonthlyReport(self):
        """
            This method is used to download Monthly report on Document --> Monthly progress report  https://labour.gov.in/ .
        """
        a = ActionChains(self.driver)
        m = self.findElementByXP("//*[@id='nav']/li[7]/a")
        # hover over element
        a.move_to_element(m).perform()
        sleep(2)
        self.findElementByXP("//*[@id='nav']/li[7]/ul/li[2]/a").click()
        sleep(2)
        self.findElementByXP(
            "//*[@id='fontSize']/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a").click()
        self.acceptAlert()
        sleep(2)
        # Switch to Parent page
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)

    def download_Images(self):
        """
            This method is used to download Images from Photo Gallery under Media Tab on  https://labour.gov.in/ .
        """
        # Click on Media --> Photo Gallery
        a1 = ActionChains(self.driver)
        m1 = self.findElementByXP("//*[@id='nav']/li[10]")
        # hover over element
        a1.move_to_element(m1).perform()
        sleep(2)
        self.findElementByXP("//*[@id='nav']/li[10]/ul/li[2]/a").click()

        path = './IMGS'
        # create new folder
        os.mkdir(path)

        # Fetching list of images
        imgResults = self.driver.find_elements(By.XPATH, "//img[contains(@typeof,'foaf:Image')]")
        src = []
        for img in imgResults:
            src.append(img.get_attribute('src'))
        # Download images from the src[] which has image url
        for i in range(10):
            response = requests.get(src[i])
            with open(f"D:/PAT24WE/IMGS/images{i + 1}.jpg", "wb") as f:
                f.write(response.content)

    def closePopUp(self):
        self.findElementByXP("//*[@id='popup']/div[2]/button").click()

    def acceptAlert(self):
        sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        sleep(2)


obj1 = Labour()
obj1.boot()
obj1.closePopUp()
obj1.download_MonthlyReport()
obj1.download_Images()

