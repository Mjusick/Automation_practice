from pages.base_page import BasePage


class MyAccountPage(BasePage):
    URL = "http://automationpractice.com/index.php?controller=my-account"

    def is_at(self):
        return self.driver.current_url == self.URL
