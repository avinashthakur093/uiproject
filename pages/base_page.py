import abc
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config
from utils.logger import logger

class BasePage(abc.ABC):
    """An abstract base class used for navigation from https://demoqa.com to specific pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.shortTimeout)


    @abc.abstractmethod
    def navigate(self):
        """
        Abstract function, to be used for navigation from demoqa homepage to different pages.
        """
        pass

    def find_element(self, by, locator, parent=None, timeout=Config.shortTimeout):
        """
        Find an element with retry and timeout handling with optional parent scoping.
        """
        try:
            if parent:
                return WebDriverWait(parent, Config.shortTimeout).until(EC.presence_of_element_located((by, locator)))
            else:
                return self.wait.until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            logger.error(f"Element not found: {locator}")
            return None

    def click_element(self, web_element_or_by, locator=None, timeout=Config.shortTimeout):
        """
        Clicks an element with handling for overlaps and timeouts.
        """
        try:
            if locator:
                element = self.wait.until(EC.element_to_be_clickable((web_element_or_by, locator)))
            else:
                element = self.wait.until(EC.element_to_be_clickable(web_element_or_by))
            element.click()
        except ElementClickInterceptedException:
            logger.warning(f"Element {locator} is not clickable, attempting via JavaScript")
            self.driver.execute_script("arguments[0].click();", element)
        except TimeoutException:
            logger.error(f"Timed out waiting for {locator} to be clickable")

    def wait_for_element_disappear(self, by, locator, timeout=Config.shortTimeout):
        """
        Waits for an element to disappear from the DOM.
        """
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            logger.warning(f"Element {locator} did not disappear in time")

    def is_element_present(self, by, locator):
        """
        Check if an element is present in the DOM.
        """
        try:
            self.driver.find_element(by, locator)
            return True
        except NoSuchElementException:
            return False