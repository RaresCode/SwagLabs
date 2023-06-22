from selenium import webdriver
import logging

def get_logger(name):
    #CREATE LOG INTO THE Logs Folder
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    log_file = f'../Logs/{name}.log'
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    
    # RETURN THE LOGGER
    return logger

def create_screenshot(driver, name):
    # CREATE SCREENSHOT OF THE POSITION
    screenshot_path = f'../Screenshots/{name}.png'
    driver.save_screenshot(screenshot_path)
