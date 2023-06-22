from PageObjects.Login import Login
from PageObjects.Products import Products
from database.db_connect import DatabaseConnector
from TestCases.logger import get_logger
from TestCases.logger import create_screenshot
import pytest

class SetupTests:
    
    @pytest.fixture
    def login_standard(self, driver, expected_wait):
        """
        Fixture for standard login process.
        """
        self.driver = driver
        
        login = Login(self.driver, expected_wait)
        login.open_webpage()
        login.input_username()
        login.input_password()
        login.click_submit()

        yield login

        login.close_browser()
    
    @pytest.fixture
    def set_logger(self):
        self.test_name = self.__class__.__name__
        self.logger = get_logger(self.test_name)

    def take_screenshot(self):
        create_screenshot(self.driver, self.__class__.__name__)
        
    @pytest.fixture
    def setup_db(self):
        """
        Fixture for setting up the database connection.
        """
        self.database = DatabaseConnector()
    
    @pytest.fixture
    def get_products(self, expected_wait):
        """
        Fixture for retrieving products data.
        """
        self.products_db = self.database.get_products_data_names_asc()
        self.products = Products(expected_wait)
        
    @pytest.fixture
    def get_product_names_db(self):
        """
        Fixture for retrieving product names from the database.
        """
        self.item_names_db = [item_name[1] for item_name in self.products_db]
    
    @pytest.fixture
    def get_product_names_webpage(self):
        """
        Fixture for retrieving product names from the webpage.
        """
        self.item_names_webpage = self.products.get_item_names()
    

class Test_Products_Names_ASCENDING(SetupTests):
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_products_names_asc(self, login_standard, set_logger, setup_db, get_products, get_product_names_db, get_product_names_webpage):
        if self.item_names_db == self.item_names_webpage:
            self.logger.info(f"Test '{self.test_name}' passed")
        else:
            self.logger.error(f"Test '{self.test_name}' failed")
            self.take_screenshot()
            
        assert self.item_names_db == self.item_names_webpage

class Test_Products_Names_DESCENDING(SetupTests):
    
    @pytest.fixture
    def get_products(self, expected_wait):
        """
        Fixture for retrieving products data.
        """
        self.products_db = self.database.get_products_data_names_desc()
        self.products = Products(expected_wait)
        
    
    @pytest.fixture
    def get_product_names_webpage(self):
        """
        Fixture for retrieving product names from the webpage.
        """
        self.products.sort_name_descending()
        self.item_names_webpage = self.products.get_item_names()
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_products_names_desc(self, login_standard, set_logger, setup_db, get_products, get_product_names_db, get_product_names_webpage):
        if self.item_names_db == self.item_names_webpage:
            self.logger.info(f"Test '{self.test_name}' passed")
        else:
            self.logger.error(f"Test '{self.test_name}' failed")
            self.take_screenshot()
            
        assert self.item_names_db == self.item_names_webpage

class Test_Products_Names_Prices_DESCENDING(SetupTests):
    
    @pytest.fixture
    def get_products(self, expected_wait):
        """
        Fixture for retrieving products data.
        """
        self.products_db = self.database.get_products_data_price_asc()
        self.products = Products(expected_wait)
        
    @pytest.fixture
    def get_product_names_webpage(self):
        """
        Fixture for retrieving product names from the webpage.
        """
        self.products.sort_price_ascending()
        self.item_names_webpage = self.products.get_item_names()
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_products_prices_asc(self, login_standard, set_logger, setup_db, get_products, get_product_names_db, get_product_names_webpage):
        if self.item_names_db == self.item_names_webpage:
            self.logger.info(f"Test '{self.test_name}' passed")
        else:
            self.logger.error(f"Test '{self.test_name}' failed")
            self.take_screenshot()
            
        assert self.item_names_db == self.item_names_webpage

class Test_Products_Names_Prices_ASCENDING(SetupTests):
    
    @pytest.fixture
    def get_products(self, expected_wait):
        """
        Fixture for retrieving products data.
        """
        self.products_db = self.database.get_products_data_price_desc()
        self.products = Products(expected_wait)
    
    @pytest.fixture
    def get_product_names_webpage(self):
        """
        Fixture for retrieving product names from the webpage.
        """
        self.products.sort_price_descending()
        self.item_names_webpage = self.products.get_item_names()
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_products_prices_desc(self, login_standard, set_logger, setup_db, get_products, get_product_names_db, get_product_names_webpage):
        if self.item_names_db == self.item_names_webpage:
            self.logger.info(f"Test '{self.test_name}' passed")
        else:
            self.logger.error(f"Test '{self.test_name}' failed")
            self.take_screenshot()
            
        assert self.item_names_db == self.item_names_webpage