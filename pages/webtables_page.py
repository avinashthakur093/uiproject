from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from datetime import datetime
import random
from pages.home_page import HomePage
from pages.elements_page import ElementsPage
from pages.base_page import BasePage


class WebTablesPage(BasePage):
    ADD_ROW_BUTTON = "//button[@id='addNewRecordButton']"
    FIRST_NAME = "//input[@id='firstName']"
    LAST_NAME = "//input[@id='lastName']"
    EMAIL = "//input[@id='userEmail']"
    AGE = "//input[@id='age']"
    SALARY = "//input[@id='salary']"
    DEPARTMENT = "//input[@id='department']"
    SUBMIT_BUTTON = "//button[@id='submit']"
    DISABLED_PREVIOUS_BUTTON = "//button[@disabled and text()='Previous']"
    DISABLED_NEXT_BUTTON = "//button[@disabled and text()='Next']"
    PREVIOUS_BUTTON = "//button[contains(text(), 'Previous')]"
    NEXT_BUTTON = "//button[contains(text(), 'Next')]"
    PAGE_INFO_ELEMENT = "//span[@class='-pageInfo']"
    TOTAL_PAGES_COUNT = "//span[@class='-totalPages']"
    PAGE_SIZE_COMBO_BOX = "//span[@class='select-wrap -pageSizeOptions']"
    DEFAULT_PAGE = "//input[@aria-label='jump to page' and @value='1']"
    SCROLL_INTO_VIEW = "arguments[0].scrollIntoView(true);"
    SELECT_PAGE_SIZE = "//option[@value={page_size}]"
    TABLE_ROWS = "//div[@class='rt-tr-group']"

    def __init__(self, driver):
        super().__init__(driver)
        self.add_row_btn = (By.XPATH, self.ADD_ROW_BUTTON)
        # Registration Form:
        self.first_name = (By.XPATH, self.FIRST_NAME)
        self.last_name = (By.XPATH, self.LAST_NAME)
        self.email = (By.XPATH, self.EMAIL)
        self.age = (By.XPATH, self.AGE)
        self.salary = (By.XPATH, self.SALARY)
        self.department = (By.XPATH, self.DEPARTMENT)
        # self.submit_btn = (By.XPATH, self.SUBMIT_BUTTON)
        self.fake_data = Faker()

    def navigate(self):
        """
        Function navigate to Web Tables Page.
        :param: None
        :return: None
        """
        home_page = HomePage(self.driver)
        home_page.click_elements()
        elements_page = ElementsPage(self.driver)
        elements_page.click_web_tables()

    def add_new_rows(self, rows=3):
        """
        Function to add specific number of rows with valid user details
        :param rows: Number of rows to be added.
        :return: None
        """
        for row in range(0, rows):
            self.wait.until(EC.element_to_be_clickable(self.add_row_btn)).click()
            self.wait.until(
                EC.presence_of_element_located(self.first_name)).send_keys(self.fake_data.first_name())
            self.wait.until(
                EC.presence_of_element_located(self.last_name)).send_keys(self.fake_data.last_name())
            self.wait.until(EC.presence_of_element_located(self.email)).send_keys(
                self.fake_data.email())
            birth_year = self.fake_data.date_of_birth(minimum_age=18, maximum_age=58).year
            age = datetime.now().year - birth_year
            self.wait.until(EC.presence_of_element_located(self.age)).send_keys(
                str(age))
            self.wait.until(
                EC.presence_of_element_located(self.salary)).send_keys(str(random.randint(5000, 100000)))
            self.wait.until(
                EC.presence_of_element_located(self.department)).send_keys("Technology")
            self.click_element(By.XPATH, self.SUBMIT_BUTTON)

    def element_is_visible(self, element_to_be_checked: tuple[str, str]):
        """
        Function to check if element is visible
        :param element_to_be_checked: element which has to be checked
        :return: True if element is visible else False
        """
        element = self.wait.until(EC.visibility_of_element_located(element_to_be_checked))
        return element.is_displayed()

    def get_total_page_count(self):
        """
        Function to return total number of pages available under pagination
        :param
        :return: Returns total number pages
        """

        # scroll to page count element, before getting the count
        # total_page_count_element = self.driver.find_element(By.XPATH, self.TOTAL_PAGES_COUNT)
        total_page_count_element = self.find_element(By.XPATH, self.TOTAL_PAGES_COUNT)
        self.driver.execute_script(self.SCROLL_INTO_VIEW, total_page_count_element)
        # Locate the span element by xpath using class name
        # element = self.driver.find_element(By.XPATH, self.TOTAL_PAGES_COUNT)
        element = self.find_element(By.XPATH, self.TOTAL_PAGES_COUNT)

        # Get the text from the element
        if element is not None:
            page_count = element.text
            return int(page_count)
        return 0
