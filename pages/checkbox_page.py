from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.all_page_objects import GenericObjects, CheckboxPageObjects
from pages.base_page import BasePage
from pages.elements_page import ElementsPage
from utils.logger import logger
from config import Config


class CheckboxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.expand_buttons = (By.XPATH, CheckboxPageObjects.EXPAND_BUTTONS)
        self.expand_all_buttons = (By.XPATH, CheckboxPageObjects.EXPAND_ALL_BUTTONS)
        self.EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, CheckboxPageObjects.EXPAND_ALL_BUTTON)
        self.CHECKBOX_TOGGLE_BUTTONS = (By.CSS_SELECTOR, CheckboxPageObjects.CHECKBOX_TOGGLE_BUTTONS)
        self.HOME_CHECKBOX = (By.XPATH, CheckboxPageObjects.HOME_CHECKBOX)

    def navigate(self):
        """
        Function navigates to Checkbox page
        """
        elements_page = ElementsPage(self.driver)
        elements_page.navigate()
        elements_page.click_checkbox()

    def expand_checkbox(self):
        """
        Expand checkbox at all level.
        :return: Returns True if collapsed checkbox exists, else False
        """
        WebDriverWait(self.driver, Config.shortTimeout).until((EC.element_to_be_clickable(self.HOME_CHECKBOX))).click()
        level2_checkboxes = self.driver.find_elements(By.XPATH, CheckboxPageObjects.CHECKBOX_SHRINKED)
        count = 0
        for element in range(0, len(level2_checkboxes)):
            self.driver.execute_script(GenericObjects.SCROLL_INTO_VIEW, level2_checkboxes[element])
            WebDriverWait(self.driver, Config.shortTimeout).until(
                EC.element_to_be_clickable(level2_checkboxes[element])).click()
            # check if level2 checkboxes have children, if yes expand.
            level3_checkboxes = self.driver.find_elements(By.XPATH, CheckboxPageObjects.CHECKBOX_SHRINKED)
            count += 1
            # first expand all the level2 checkboxes and then go for level3 checkboxes
            if count == len(level2_checkboxes) and len(level3_checkboxes) > 0:
                logger.info(f"Level3 Checkbox Element Count: {len(level3_checkboxes)}")
                for child_element in level3_checkboxes:
                    WebDriverWait(self.driver, Config.shortTimeout).until(
                        EC.element_to_be_clickable(child_element)).click()
        # find if any collapsed checkbox exist after expanding all.
        collapsed_checkbox = self.driver.find_elements(By.XPATH, CheckboxPageObjects.CHECKBOX_SHRINKED)
        if len(collapsed_checkbox) == 0:
            return True
        else:
            return False

    def expand_level2_checkbox(self, level2_checkbox_label=None):
        """
        Expand Level2 checkbox, and it's child nodes
        :param level2_checkbox_label: Accepts Level2 Checkboxes labels which are Desktop, Documents, Downloads
        """
        level2_check_box_xpath = f"//span[text()='{level2_checkbox_label}']"
        logger.info(f"Checking if {level2_checkbox_label} checkbox and it's all child nodes are selected")
        # Wait for the "Desktop" checkbox to be clickable and click it
        level2_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, level2_check_box_xpath))
        )
        level2_checkbox.click()
        # Find all child checkboxes under {level2_checkbox_label}
        child_checkboxes = self.driver.find_elements(By.XPATH,
                                                     f"//span[text()='{level2_checkbox_label}']/ancestor::li[1]//span["
                                                     f"@class='rct-checkbox']")

        # Assert that all child checkboxes are selected
        for checkbox in child_checkboxes:
            # Locate the <svg> tag inside the checkbox <span>
            svg_element = checkbox.find_element(By.XPATH, CheckboxPageObjects.SELECTED_CHECKBOX)
            assert "rct-icon-check" in svg_element.get_attribute(
                "class"), f"Checkbox is not selected: {
            checkbox.find_element(By.XPATH, CheckboxPageObjects.SELECTED_CHECKBOX_TEXT).text}"

        logger.info(f"All child checkboxes are selected!")

    def expand_private_checkbox(self):
        """
        Select Home > Documents > Office > Private checkbox and assert that the correct icons are displayed.
        :return: Returns True if Home > Documents > Office > Private checkbox is selected, else False
        """
        home_checkbox_partial_check_xpath = CheckboxPageObjects.HOME_CHECKBOX_PARTIAL_CHECK_XPATH
        documents_checkbox_partial_check_xpath = CheckboxPageObjects.DOCUMENTS_CHECKBOX_PARTIAL_CHECK_XPATH
        office_checkbox_partial_check_xpath = CheckboxPageObjects.OFFICE_CHECKBOX_PARTIAL_CHECK_XPATH
        private_checkbox_xpath = CheckboxPageObjects.PRIVATE_CHECKBOX_XPATH
        checked_private_checkbox_xpath = CheckboxPageObjects.CHECKED_PRIVATE_CHECKBOX_XPATH
        all_elements_list = [home_checkbox_partial_check_xpath,
                             documents_checkbox_partial_check_xpath,
                             office_checkbox_partial_check_xpath,
                             checked_private_checkbox_xpath]
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                         private_checkbox_xpath))).click()
        flag = True
        for element in all_elements_list:
            logger.info(f"Checking for xpath: {element}")
            if element.startswith("label"):
                selected_node_len = len(self.driver.find_elements(By.CSS_SELECTOR, element))
            else:
                selected_node_len = len(self.driver.find_elements(By.XPATH, element))
            if selected_node_len == 0:
                logger.info(f"Length of selected checkbox: {element} is 0")
                flag = False
        return flag
