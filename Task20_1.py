from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Cowin:
    """
    This class is used to work on https://www.cowin.gov.in/
    """


    def __init__(self, url="https://www.cowin.gov.in/", username="standard_user", password="secret_sauce"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
        This method is used to open the browser and go to https://www.cowin.gov.in/ .
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(3)

    def findElementByXP(self, value):
        return self.driver.find_element(by=By.XPATH, value=value)

    def openwindows(self):
        """
        This method is used to open different tabs on  https://www.cowin.gov.in/ .
        """



        # Click on FAQ hyperlink
        self.findElementByXP("//*[@id='navbar']/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a").click()
        sleep(2)

        # Switch to Parent page
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)

        # Click on Partners hyperlink
        self.findElementByXP("//*[@id='navbar']/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a").click()
        sleep(2)

        # Switch to Parent page
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)

    def getWinId_closeChildTab(self):
        # Get ID of main window
        parent_guid = self.driver.current_window_handle
        # Get ID of all windows in list
        all_winid = self.driver.window_handles
        # iterate through the window ID  and if there is a parent window id skip it and switch to the new window
        for winid in all_winid:
            if winid != parent_guid:
                self.driver.switch_to.window(winid)
                sleep(3)
                print(f"The Window ID of child is : {winid}")
                self.driver.close()
                sleep(3)


obj1 = Cowin()
obj1.boot()
obj1.openwindows()
obj1.getWinId_closeChildTab()

