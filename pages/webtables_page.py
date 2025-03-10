from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from datetime import datetime
import random
from pages.home_page import HomePage
from pages.elements_page import ElementsPage
from pages.base_page import BasePage
from utils.logger import logger
from config import Config


class WebTablesPage(BasePage):
    ADD_ROW_BUTTON = "//button[@id='addNewRecordButton']"
    FIRST_NAME = "//input[@id='firstName']"
    LAST_NAME = "//input[@id='lastName']"
    EMAIL = "//input[@id='userEmail']"
    AGE = "//input[@id='age']"
    SALARY = "//input[@id='salary']"
    DEPARTMENT = "//input[@id='department']"
    SUBMIT_BUTTON = "//button[@id='submit']"
    PREVIOUS_BUTTON = "//button[contains(text(), 'Previous')]"
    NEXT_BUTTON = "//button[contains(text(), 'Next')]"
    PAGE_INFO_ELEMENT = "//span[@class='-pageInfo']"
    PAGE_SIZE_COMBO_BOX = "//span[@class='select-wrap -pageSizeOptions']"
    DEFAULT_PAGE = "//input[@aria-label='jump to page' and @value='1']"

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
        self.submit_btn = (By.XPATH, self.SUBMIT_BUTTON)
        self.fake_data = Faker()

    def navigate(self):
        """
        Function navigate to Web Tables Page.
        """
        home_page = HomePage(self.driver)
        home_page.click_elements()
        elements_page = ElementsPage(self.driver)
        elements_page.click_web_tables()

    def add_new_rows(self, rows=3):
        """
        Function to add specific number of rows with valid user details
        :param rows: Number of rows to be added.
        """
        for row in range(0, rows):
            WebDriverWait(self.driver, Config.shortTimeout).until(EC.element_to_be_clickable(self.add_row_btn)).click()
            WebDriverWait(self.driver, Config.shortTimeout).until(
                EC.presence_of_element_located(self.first_name)).send_keys(self.fake_data.first_name())
            WebDriverWait(self.driver, Config.shortTimeout).until(
                EC.presence_of_element_located(self.last_name)).send_keys(self.fake_data.last_name())
            WebDriverWait(self.driver, Config.shortTimeout).until(EC.presence_of_element_located(self.email)).send_keys(
                self.fake_data.email())
            birth_year = self.fake_data.date_of_birth(minimum_age=18, maximum_age=58).year
            age = datetime.now().year - birth_year
            WebDriverWait(self.driver, Config.shortTimeout).until(EC.presence_of_element_located(self.age)).send_keys(
                str(age))
            WebDriverWait(self.driver, Config.shortTimeout).until(
                EC.presence_of_element_located(self.salary)).send_keys(str(random.randint(5000, 100000)))
            WebDriverWait(self.driver, Config.shortTimeout).until(
                EC.presence_of_element_located(self.department)).send_keys("Technology")
            WebDriverWait(self.driver, Config.shortTimeout).until(EC.element_to_be_clickable(self.submit_btn)).click()

    def element_is_visible(self, element_to_be_checked: tuple[str, str]):
        """
        Function to check if element is visible
        :param element_to_be_checked: element which has to be checked
        :return: True if element is visible else False
        """
        element = WebDriverWait(self.driver, Config.shortTimeout).until(EC.visibility_of_element_located(
            element_to_be_checked))
        return element.is_displayed()
