from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    PHONE_NUMBER = (By.XPATH, '//span[@class=\'shop-phone\']/strong')
    SIGN_IN_BUTTON = (By.XPATH, '//a[@class=\'login\']')

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER).text

    def click_sign_in_button(self):
        sign_in_button = self.driver.find_element(*self.SIGN_IN_BUTTON)
        sign_in_button.click()
