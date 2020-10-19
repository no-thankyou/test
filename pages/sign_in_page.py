from pages.base_page import BasePage
from pages.locators import BasePageLocators, RegisterLocators


class SigninPage(BasePage):
    def should_be_sign_in_page(self):
        self.should_be_sign_in_url()
        self.should_be_email_form()
        self.should_be_create_an_account_button()

    def should_be_sign_in_url(self):
        assert "sign in" in self.browser.current_url, "'sign in' not in current url"

    def should_be_email_form(self):
        assert self.is_element_present(*BasePageLocators.EMAIL_FIELD), \
            "Email form is not presented"

    def should_be_create_an_account_button(self):
        assert self.is_element_present(*BasePageLocators.CREATE_AN_ACCOUNT), \
            "Create an account button is not presented"

    def register_new_user(self):
        self.browser.find_element(*RegisterLocators.FIRST_NAME).send_keys('name'),
        self.browser.find_element(*RegisterLocators.LAST_NAME).send_keys("lastname"),
        self.browser.find_element(*RegisterLocators.PASSWORD).send_keys("123456"),
        self.browser.find_element(*RegisterLocators.ADDRESS).send_keys("address"),
        self.browser.find_element(*RegisterLocators.CITY).send_keys("City"),
        self.browser.find_element(*RegisterLocators.COUNTRY),
        self.browser.find_element(*RegisterLocators.MOBILE_PHONE).send_keys("78346987"),
        self.browser.find_element(*RegisterLocators.ALIAS)).send_keys('sometheing'),
        self.browser.find_element(*RegisterLocators.REGISTER).click()
