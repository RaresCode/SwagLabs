from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Products:
    
    item_names_class = "inventory_item_name"
    item_prices_class = "inventory_item_price"
    item_descriptions_class = "inventory_item_desc"
    items_add_cart_id = "add-to-cart"
    sort_dropdown = "product_sort_container"


    def __init__(self, expected_wait):
        self.expected_wait = expected_wait
        
    # def add_items_to_cart(self):
    #     all_items = self.WebDriverWait.until(EC.presence_of_all_elements_located((By.ID , self.items_add_cart_id)))
    #     return [item.click for item in all_items]
    
    def get_item_names(self):
        item_names = self.expected_wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , self.item_names_class)))
        return [item.text for item in item_names]

    def get_item_prices(self):
        item_prices = self.expected_wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , self.item_prices_class)))
        return [float(item.text[1:]) for item in item_prices]
        
    def get_item_desc(self):
        item_desc = self.expected_wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , self.item_descriptions_class)))
        return [item.text for item in item_desc]
    
    def sort_name_descending(self):
        Select(self.expected_wait.until(EC.visibility_of_element_located((By.CLASS_NAME , self.sort_dropdown)))).select_by_value('za')
        
    def sort_price_ascending(self):
        Select(self.expected_wait.until(EC.visibility_of_element_located((By.CLASS_NAME , self.sort_dropdown)))).select_by_value('lohi') 
    
    def sort_price_descending(self):
        Select(self.expected_wait.until(EC.visibility_of_element_located((By.CLASS_NAME , self.sort_dropdown)))).select_by_value('hilo') 


