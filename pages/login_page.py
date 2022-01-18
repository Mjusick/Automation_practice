from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    CREATE_ACC_EMAIL_ADDRESS_FIELD = (By.ID, 'email_create')
    CREATE_ACC_SUBMIT_BUTTON = (By.ID, 'SubmitCreate')

    def create_account(self, client):
        email_address_field = self.driver.find_element(*self.CREATE_ACC_EMAIL_ADDRESS_FIELD)
        submit_button = self.driver.find_element(*self.CREATE_ACC_SUBMIT_BUTTON)

        email_address_field.click()
        email_address_field.send_keys(client.email)
        submit_button.click()
