from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.home_page import HomePage


class ElementsPage(BasePage):
    CHECKBOX_LINK = "//span[text()='Check Box']"
    WEB_TABLES_LINK = "//span[text()='Web Tables']"
    DYNAMIC_PROPERTIES_LINK = "//span[text()='Dynamic Properties']"
    BOOK_STORE_APP_LINK = "//div[text()='Book Store Application']"
    BOOK_STORE_LINK = "//span[text()='Book Store']"

    def __init__(self, driver):
        super().__init__(driver)
        self.checkbox_link = (By.XPATH, self.CHECKBOX_LINK)
        self.webtables_link = (By.XPATH, self.WEB_TABLES_LINK)
        self.dynamic_properties = (By.XPATH, self.DYNAMIC_PROPERTIES_LINK)
        self.book_store_app = (By.XPATH, self.BOOK_STORE_APP_LINK)
        self.book_store = (By.XPATH, self.BOOK_STORE_LINK)

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
        self.click_element(self.checkbox_link[0], self.checkbox_link[1])
    def click_web_tables(self):
        """
        Navigate from Elements > Web Tables
        :return:
        """
        self.click_element(self.webtables_link[0], self.webtables_link[1])
    def click_dynamic_properties(self):
        """
        Navigate from Elements > Dynamic Properties
        :return:
        """
        self.click_element(self.dynamic_properties[0], self.dynamic_properties[1])

    def click_book_store_application(self):
        """
        Navigate from Elements > Book Store Application > Book Store
        :return:
        """
        # Scroll to 'Book Store Application' in the side navigation
        book_store_nav = self.wait.until(EC.presence_of_element_located(self.book_store_app))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", book_store_nav)
        # Click on 'Book Store Application'
        self.click_element(self.book_store_app[0], self.book_store_app[1])
        # Navigate to Book Store, where Book information is available
        self.click_element(self.book_store[0], self.book_store[1])