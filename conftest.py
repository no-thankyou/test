import pytest
from selenium import webdriver


@pytest.fixture()
def browser(request):
    print("\n\nStart browser...")
    browser = webdriver.Chrome()
    yield browser
    print("\n\nQuit browser.")
    browser.quit()