from PageObjects.Login import Login
from TestCases.logger import get_logger
from TestCases.logger import create_screenshot
import pytest


class Test_Login:
    @pytest.fixture
    def open_browser(self, driver, expected_wait):
        self.driver = driver
        self.login = Login(driver, expected_wait)
        self.login.open_webpage()  # Open the webpage before each test
        
        yield self.login
        
        self.login.close_browser()  # Close the browser after each test
    
    @pytest.fixture
    def set_logger(self):
        self.test_name = self.__class__.__name__
        self.logger = get_logger(self.test_name)

    def take_screenshot(self):
        create_screenshot(self.driver, self.__class__.__name__)
    
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_login(self, open_browser, set_logger):
        self.login.input_username()  # Input the username
        self.login.input_password()  # Input the password
        self.login.click_submit()  # Click the submit button
        current_page = self.login.get_page()  # Get the current page
        
        
        if current_page == "https://www.saucedemo.com/inventory.html":
            self.logger.info(f"Test '{self.test_name}' passed")
        else:
            self.logger.error(f"Test '{self.test_name}' failed")
            self.take_screenshot()
        
        assert current_page == "https://www.saucedemo.com/inventory.html"  # Assert that the current page is the expected product URL
    
    
    