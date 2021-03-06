import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options

@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('start_maximazed')
    options.add_argument('--window-size=1920,10870')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    return options

@pytest.fixture
def get_webdriver(get_chrome_options): 
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='C:/Users/Dench/Desktop/Selenium/chromedriver.exe', options=options)
    return driver

@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'http://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    yield driver 
    driver.quit()    