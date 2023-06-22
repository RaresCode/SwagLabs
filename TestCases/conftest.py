from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from PageObjects.Login import Login
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    # Set up the service object
    service = Service(ChromeDriverManager().install())
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # For running tests in headless uncomment this
    # chrome_options.headless = True
    
    # Create the webdriver using the service object
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver


@pytest.fixture()
def expected_wait(driver):
    return WebDriverWait(driver, 10)


