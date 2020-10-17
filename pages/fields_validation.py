from pages.base_page import BasePage
from pages.locators import RegisterLocators


class FieldsValidation(BasePage):
    def should_be_register_page(self):
        self.should_be_create_an_account_url()
        self.should_be_required_fields()
        self.should_be_register_button()

    def should_be_create_an_account_url(self):
        assert "Create an account" in self.browser.current_url, "'Create an account' not in current url"

    def should_be_required_fields(self):
        assert self.register_new_user(), \
            "Required fields must be filled"

    def should_be_register_button(self):
        assert self.is_element_present(*RegisterLocators.REGISTER), \
            "'Register' button is not presented"

