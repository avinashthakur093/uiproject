from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.all_page_objects import ElementsPageObjects
from pages.base_page import BasePage
from pages.home_page import HomePage
from config import Config

class ElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkbox_link = (By.XPATH, ElementsPageObjects.CHECKBOX_LINK)
        self.webtables_link = (By.XPATH, ElementsPageObjects.WEB_TABLES_LINK)
        self.dynamic_properties = (By.XPATH, ElementsPageObjects.DYNAMIC_PROPERTIES_LINK)
        self.book_store_app = (By.XPATH, ElementsPageObjects.BOOK_STORE_APP_LINK)
        self.book_store = (By.XPATH, ElementsPageObjects.BOOK_STORE_LINK)

    def navigate(self):
        """
        Function navigates to Elements page.
        """
        home_page = HomePage(self.driver)
        home_page.click_elements()

    def click_checkbox(self):
        """
        Navigate from Elements > Checkbox
        :return:
        """
        WebDriverWait(self.driver, Config.shortTimeout).until(EC.element_to_be_clickable(self.checkbox_link)).click()

    def click_web_tables(self):
        """
        Navigate from Elements > Web Tables
        :return:
        """
        WebDriverWait(self.driver, Config.shortTimeout).until(EC.element_to_be_clickable(self.webtables_link)).click()

    def click_dynamic_properties(self):
        """
        Navigate from Elements > Dynamic Properties
        :return:
        """
        WebDriverWait(self.driver, Config.shortTimeout).until(EC.element_to_be_clickable(self.dynamic_properties)).click()

    def click_book_store_application(self):
        """
        Navigate from Elements > Book Store Application > Book Store
        :return:
        """
        wait = WebDriverWait(self.driver, Config.shortTimeout)
        # Scroll to 'Book Store Application' in the side navigation
        book_store_nav = wait.until(EC.presence_of_element_located(self.book_store_app))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", book_store_nav)
        # Click on 'Book Store Application'
        WebDriverWait(self.driver, Config.shortTimeout).until(EC.element_to_be_clickable(self.book_store_app)).click()
        # Navigate to Book Store, where Book information is available
        WebDriverWait(self.driver, Config.shortTimeout).until(EC.element_to_be_clickable(self.book_store)).click()

