import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Client import Client
from pages.base_page import BasePage

# TODO add email field to clear and assert empty field
class CreateAccountPage(BasePage):
    URL = "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation"
    TITLE_BUTTONS = (By.XPATH, "//div[@class = 'clearfix']/div[@class='radio-inline']")
    FIRST_NAME_FIELD = (By.ID, "customer_firstname")
    LAST_NAME_FIELD = (By.ID, "customer_lastname")
    PASSWORD_FIELD = (By.ID, "passwd")
    DAYS_DATE_SELECT = (By.ID, "days")
    MONTHS_DATE_SELECT = (By.ID, "months")
    YEARS_DATE_SELECT = (By.ID, "years")
    COMPANY_FIELD = (By.ID, "company")
    ADDRESS1_FIELD = (By.ID, "address1")
    ADDRESS2_FIELD = (By.ID, "address2")
    CITY_FIELD = (By.ID, "city")
    STATE_SELECT = (By.ID, "id_state")
    POSTAL_CODE_FIELD = (By.ID, "postcode")
    COUNTRY_SELECT = (By.ID, "id_country")
    OTHER_FIELD = (By.ID, "other")
    HOME_PHONE_FIELD = (By.ID, "phone")
    MOBILE_PHONE_FIELD = (By.ID, "phone_mobile")
    ALIAS_FIELD = (By.ID, "alias")
    SUBMIT_ACCOUNT_BUTTON = (By.ID, "submitAccount")
    FIELD_WITH_MISSING_PARAMETER = (By.XPATH, "//div[contains(@class,'form-error')]")
    MISSING_FIELD_ALERT_INFORMATION = (By.XPATH, "//div[@class='alert alert-danger']")

    def fill_account_form(self, client: Client):
        self.fill_first_name_field(client.first_name)
        self.fill_last_name_field(client.last_name)
        self.fill_password_field(client.password)
        self.select_date(client.birth_date)
        self.fill_company_field(client.company)
        self.fill_address1_field(client.address_1)
        self.fill_address2_field(client.address_2)
        self.fill_city_field(client.city)
        self.select_state(client.state)
        self.fill_postal_code_field(client.zipcode)
        self.fill_other_field(client.other)
        self.fill_home_number_field(client.phone)
        self.fill_mobile_phone_field(client.mobile)
        self.fill_alias(client.alias)

    def fill_account_form_with_missing_field(self, client: Client, missing_field: str):
        for field in client.__dict__:
            if field == missing_field:
                client.__dict__.update({field: ""})
        self.fill_first_name_field(client.first_name)
        self.fill_last_name_field(client.last_name)
        self.fill_password_field(client.password)
        self.select_date(client.birth_date)
        self.fill_company_field(client.company)
        self.fill_address1_field(client.address_1)
        self.fill_address2_field(client.address_2)
        self.fill_city_field(client.city)
        self.select_state(client.state)
        self.fill_postal_code_field(client.zipcode)
        self.fill_other_field(client.other)
        self.fill_home_number_field(client.phone)
        self.fill_mobile_phone_field(client.mobile)
        self.fill_alias(client.alias)

    def submit_account_form(self):
        submit_button = self.driver.find_element(*self.SUBMIT_ACCOUNT_BUTTON)
        submit_button.click()

    def choose_title(self, title: str):
        title_buttons = self.driver.find_elements(*self.TITLE_BUTTONS)
        if title == "male":
            title_buttons[0].click()
        elif title == "female":
            title_buttons[1].click()

    def fill_first_name_field(self, first_name):
        first_name_field = self.driver.find_element(*self.FIRST_NAME_FIELD)
        first_name_field.send_keys(first_name)

    def fill_last_name_field(self, last_name):
        last_name_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        last_name_field.send_keys(last_name)

    def fill_password_field(self, password):
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(password)

    def select_date(self, date: datetime.date):
        select_day = Select(self.driver.find_element(*self.DAYS_DATE_SELECT))
        select_month = Select(self.driver.find_element(*self.MONTHS_DATE_SELECT))
        select_years = Select(self.driver.find_element(*self.YEARS_DATE_SELECT))
        select_day.select_by_value(str(date.day))
        select_month.select_by_value(str(date.month))
        select_years.select_by_value(str(date.year))

    def fill_company_field(self, company_name):
        company_field = self.driver.find_element(*self.COMPANY_FIELD)
        company_field.send_keys(company_name)

    def fill_address1_field(self, address1):
        address1_field = self.driver.find_element(*self.ADDRESS1_FIELD)
        address1_field.send_keys(address1)

    def fill_address2_field(self, address2):
        address2_field = self.driver.find_element(*self.ADDRESS2_FIELD)
        address2_field.send_keys(address2)

    def fill_city_field(self, city):
        city_field = self.driver.find_element(*self.CITY_FIELD)
        city_field.send_keys(city)

    def select_state(self, state):
        state_select = Select(self.driver.find_element(*self.STATE_SELECT))
        state_select.select_by_visible_text(state)

    def fill_postal_code_field(self, postal_code):
        postal_code_field = self.driver.find_element(*self.POSTAL_CODE_FIELD)
        postal_code_field.send_keys(postal_code)

    def select_country(self, country):
        country_select = Select(self.driver.find_element(*self.COUNTRY_SELECT))
        country_select.select_by_visible_text(country)

    def fill_other_field(self, content):
        other_field = self.driver.find_element(*self.OTHER_FIELD)
        other_field.send_keys(content)

    def fill_home_number_field(self, home_number):
        home_number_field = self.driver.find_element(*self.HOME_PHONE_FIELD)
        home_number_field.send_keys(home_number)

    def fill_mobile_phone_field(self, mobile_phone):
        mobile_phone_field = self.driver.find_element(*self.MOBILE_PHONE_FIELD)
        mobile_phone_field.send_keys(mobile_phone)

    def fill_alias(self, alias):
        alias_field = self.driver.find_element(*self.ALIAS_FIELD)
        alias_field.clear()
        alias_field.send_keys(alias)

    def field_name_with_missing_parameter(self):
        missing_parameter_field = self.driver.find_element(*self.FIELD_WITH_MISSING_PARAMETER)
        return missing_parameter_field.text

    def get_error_text(self):
        error_information = self.driver.find_element(*self.MISSING_FIELD_ALERT_INFORMATION)
        return error_information.text

    def is_at(self):
        return self.driver.current_url == self.URL
