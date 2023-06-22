from PageObjects.Login import Login
from PageObjects.Checkout import Checkout
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
        login.open_webpage()  # Open the webpage
        login.input_username()  # Input the username
        login.input_password()  # Input the password
        login.click_submit()  # Click the submit button

        self.checkout = Checkout(expected_wait)  # Create a Checkout instance

        yield login

        login.close_browser()  # Close the browser

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


class Test_Checkout(SetupTests):

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_checkout(self, login_standard, set_logger):
        """
        Test case for the checkout process.
        """
        self.checkout.add_item()  # Add item to the checkout
        self.checkout.open_checkout()  # Open the checkout page
        self.checkout.click_continue_checkout()  # Click the continue checkout button
        self.checkout.input_first_name()  # Input the first name
        self.checkout.input_last_name()  # Input the last name
        self.checkout.input_zip_code()  # Input the ZIP code
        self.checkout.click_continue_checkout_info()  # Click the continue checkout info button
        self.checkout.click_finish()  # Click the finish button
        confirmation_msg = self.checkout.get_confirmation_msg()  # Get the confirmation message

        if confirmation_msg == "Your order has been dispatched, and will arrive just as fast as the pony can get there!":
            self.logger.info(f"Test '{self.test_name}' passed")
        else:
            self.logger.error(f"Test '{self.test_name}' failed")
            self.take_screenshot()
            
        assert confirmation_msg == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

class Test_Checkout_DB(SetupTests):

    @pytest.fixture
    def order_data(self):
        """
        Fixture for order data.
        """
        return {
            "first_name": "Marian",
            "last_name": "Popescu",
            "zip_code": "37000"
        }

    @pytest.fixture
    def order_db_management(self, order_data):
        """
        Fixture for managing the database entries.
        """
        self.database.add_order_details(order_data["first_name"], order_data["last_name"], order_data["zip_code"])  # Add order details
        yield
        self.database.delete_order(order_data["first_name"], order_data["last_name"], order_data["zip_code"])  # Delete order


    @pytest.mark.regression
    @pytest.mark.smoke
    def test_bought_item_entry(self, set_logger, setup_db, order_data, order_db_management):
        """
        Test case for verifying the database entry after buying an item.
        """
        db_item_entry = self.database.get_order(order_data["first_name"], order_data["last_name"], order_data["zip_code"])  # Get the database entry

        if (order_data["first_name"], order_data["last_name"], order_data["zip_code"]) == db_item_entry:
            self.logger.info(f"Test '{self.test_name}' passed")
        else:
            self.logger.error(f"Test '{self.test_name}' failed")

        assert (order_data["first_name"], order_data["last_name"], order_data["zip_code"]) == db_item_entry