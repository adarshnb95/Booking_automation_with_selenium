import os
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r"C:\Drivers\chromedriver-win64\chromedriver.exe", teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()
    
    def land_First_Page(self):
        self.get(const.BASE_URL)

    def dismiss_Offer(self):
        WebDriverWait(self, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")))
        close_button = self.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")
        close_button.click()
    

    def change_currency(self, currency = None):
        currency_element = self.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")
        currency_element.click()
        selected_currency_element = self.find_element(By.XPATH, "//*[@id='b2indexPage']/div[21]/div/div/div/div/div[2]/div/div[2]/div/div/ul[1]/li[1]/button")
        selected_currency_element.click()

        # //*[@id="b2indexPage"]/div[21]/div/div/div/div/div[2]/div/div[2]/div/div/ul[1]/li[1]/button/div

        # //*[@id="b2indexPage"]/div[21]/div/div/div/div/div[2]/div/div[2]/div/div/ul[1]/li[1]/button

        # /html/body/div[21]/div/div/div/div/div[2]/div/div[2]/div/div/ul[1]/li[1]/button/div/div[1]/span/text()
