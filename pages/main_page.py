from .base_page import BasePage
from .locators import BasePageLocators
from .sign_in_page import SigninPage


class MainPage(BasePage):
    def sign_in_link(self):
        sigh_in = self.browser.find_element(*BasePageLocators.SIGN_IN_LINK)
        sigh_in.click()
        return SigninPage(browser=self.browser, url=self.browser.current_url)

    def input_email(self):
        example_email = 'mail@mail.ru'
        email_field = self.browser.find_element(*BasePageLocators.EMAIL_FIELD)
        input_data = self.browser.send_keys(example_email)
        self.browser.find_element(*BasePageLocators.CREATE_AN_ACCOUNT).click()