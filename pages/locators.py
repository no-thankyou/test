from selenium.webdriver.common.by import By


class BasePageLocators:
    SIGN_IN_LINK = (By.XPATH, "//a[@class='login']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='email_create']")
    CREATE_AN_ACCOUNT = (By.XPATH, "//button[@id='SubmitCreate']")


class RegisterLocators:
    FIRST_NAME = (By.XPATH, "//input[@id='customer_firstname']")
    LAST_NAME = (By.XPATH, "//input[@id='customer_lastname']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='passwd']")
    REGISTER = (By.XPATH, "//button[@id='submitAccount']")
    ADDRESS = (By.XPATH, "//input[@id='address1']")
    CITY = (By.XPATH, "//select[@id='id_country']/option[@value='21']")
    COUNTRY = (By.XPATH, "//select[@id='id_country']")
    MOBILE_PHONE = (By.XPATH, "//input[@id='phone_mobile']")
    ALIAS = (By.XPATH, "//input[@id='alias']")