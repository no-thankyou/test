from pages.main_page import MainPage


class TestSignInPage(MainPage):

    def test_user_can_see_sign_in_link(self, browser):
        link = "http://automationpractice.com/index.php"
        page = MainPage(browser, link)
        page.open()
        page.should_be_sign_in_link()

    def test_user_can_go_to_sign_in_page(self, browser):
        link = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
        page = MainPage(browser, link)
        page.open()
        sign_in_page = page.sign_in_link()
        sign_in_page.should_be_sign_in_page()

    def test_user_can_input_email(self, browser):
        link = "http://automationpractice.com/index.php"
        page = MainPage(browser, link)
        page.open()
        page.input_email()


class TestFieldsValidation(MainPage):

    def test_user_can_register(self, browser):
        link = "http://automationpractice.com/index.php"
        page = MainPage(browser, link)
        page.open()
        page.input_email()
        page.should_be_register_page()



