from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeatsPage:
    def __init__(self, driver):
        self.driver = driver

    #Locators:

    seat_one = (AppiumBy.XPATH, '//android.widget.TextView[@text="2"]')
    seat_seven = (AppiumBy.XPATH, '//android.widget.TextView[@text="3"]')

    continue_button = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "Continuar con")]')

    #Methods

    def select_seat_one(self):
        origin_element = WebDriverWait(self.driver, 15).until(
        EC.visibility_of_element_located(self.seat_one))
        origin_element.click()
        self.driver.find_element(*self.continue_button).click()

    def select_seat_seven(self):
        origin_element = WebDriverWait(self.driver, 15).until(
        EC.visibility_of_element_located(self.seat_seven))
        origin_element.click()
        self.driver.find_element(*self.continue_button).click()




