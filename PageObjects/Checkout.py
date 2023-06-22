from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Checkout:
    
    first_item = "*/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button"
    checkout_link = "shopping_cart_link"
    continue_checkout = "checkout"
    first_name_field = "first-name"
    last_name_field = "last-name"
    zip_code_field = "postal-code"
    continue_checkout_info = "continue"
    finish_checkout = "finish"
    confirmation_msg = "complete-text"

    def __init__(self, expected_wait):
        self.expected_wait = expected_wait

    def add_item(self):
        self.expected_wait.until(EC.element_to_be_clickable((By.XPATH , self.first_item))).click()
    
    def open_checkout(self):
        self.expected_wait.until(EC.visibility_of_element_located((By.CLASS_NAME , self.checkout_link))).click()
    
    def click_continue_checkout(self):
        self.expected_wait.until(EC.element_to_be_clickable((By.ID , self.continue_checkout))).click()
    
    def input_first_name(self):
        self.expected_wait.until(EC.presence_of_element_located((By.ID , self.first_name_field))).send_keys("Marian")
        
    def input_last_name(self):
        self.expected_wait.until(EC.presence_of_element_located((By.ID , self.last_name_field))).send_keys("Popescu")
    
    def input_zip_code(self):
        self.expected_wait.until(EC.presence_of_element_located((By.ID , self.zip_code_field))).send_keys("37000")
    
    def click_continue_checkout_info(self):
        self.expected_wait.until(EC.element_to_be_clickable((By.ID , self.continue_checkout_info))).click()
    
    def click_finish(self):
        self.expected_wait.until(EC.element_to_be_clickable((By.ID , self.finish_checkout))).click()
    
    def get_confirmation_msg(self):
        return self.expected_wait.until(EC.visibility_of_element_located((By.CLASS_NAME , self.confirmation_msg))).text