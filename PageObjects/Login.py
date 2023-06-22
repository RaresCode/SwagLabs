from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login:
    
    username_input_id = "user-name"
    password_input_id = "password"
    submit_btn_id = "login-button"
    login_url = "https://www.saucedemo.com/"
    
    def __init__(self, driver, expected_wait):
        self.driver = driver
        self.expected_wait = expected_wait
        
    def open_webpage(self):
        self.driver.get(self.login_url)
        
    def input_username(self):
        self.expected_wait.until(EC.presence_of_element_located((By.ID , self.username_input_id))).send_keys("standard_user")
        
    def input_password(self):
        self.expected_wait.until(EC.presence_of_element_located((By.ID , self.password_input_id))).send_keys("secret_sauce")
        
    def click_submit(self):
        self.expected_wait.until(EC.presence_of_element_located((By.ID , self.submit_btn_id))).click()
        
    def close_browser(self):
        self.driver.quit()
        
    
        
    def get_page(self):
        return self.driver.current_url