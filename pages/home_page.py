from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.all_page_objects import HomePageObjects
from pages.base_page import BasePage
from utils.logger import logger
from config import Config


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.elements_link = (By.XPATH, HomePageObjects.ELEMENTS_LINK)

    def navigate(self):
        pass  # Already on homepage

    def click_elements(self):
        logger.info("Clicking on Elements section")
        element = WebDriverWait(self.driver, Config.shortTimeout).until(
            EC.element_to_be_clickable(self.elements_link)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)  # Scroll into view
        self.driver.execute_script("arguments[0].click();", element)  # Use JavaScript click if necessary
