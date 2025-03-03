from selenium import webdriver
from config import Config
from utils.logger import logger


def setup_driver(browser):
    """Setup WebDriver based on the chosen browser."""
    if browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get(Config.baseUrl)
    logger.info(f"Launched {browser} and opened {Config.baseUrl}")
    yield driver
    driver.quit()
    logger.info(f"Closed {browser}")
