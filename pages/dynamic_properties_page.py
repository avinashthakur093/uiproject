from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.elements_page import ElementsPage
from page_objects.all_page_objects import GenericObjects, DynamicPropertiesPageObjects
from utils.logger import logger
from config import Config


class DynamicPropertiesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.enable_after_5s_btn = (By.XPATH, DynamicPropertiesPageObjects.ENABLE_AFTER_5S_BTN)
        self.color_change_btn = (By.XPATH, DynamicPropertiesPageObjects.COLOR_CHANGE_BTN)
        self.visible_after_5s_btn = (By.XPATH, DynamicPropertiesPageObjects.VISIBLE_AFTER_5S_BTN)


    def navigate(self):
        """
        Function navigates to Dynamic Properties Page
        :return:
        """
        elements_page = ElementsPage(self.driver)
        elements_page.navigate()
        elements_page.click_dynamic_properties()

    def wait_for_elements_visibility(self):
        """
        Function to fluently wait for 10s max and check if button having text 'Visible After 5 Seconds' is visible.
        This will check every 0.5s for button visiblity.
        """
        # a.	Fluently wait for button with text “Visible after 5 seconds” to be displayed
        # Fluent Wait: Poll every 500ms until the button is visible (max 10 seconds)
        wait = WebDriverWait(self.driver, Config.shortTimeout, poll_frequency=0.5)
        button = wait.until(EC.visibility_of_element_located(self.visible_after_5s_btn))
        # Assert that the button is displayed
        assert button.is_displayed(), "Button is not visible after waiting."

        # b.	Refresh the page and verify that the second button changes color after some time
        color_btn = self.driver.find_element(self.color_change_btn[0], self.color_change_btn[1])
        initial_color = color_btn.value_of_css_property("color")
        # Refresh the page
        self.driver.refresh()
        color_btn = wait.until(EC.presence_of_element_located((self.color_change_btn[0], self.color_change_btn[1])))
        logger.info(f"Initial Color: {initial_color}")
        wait.until(lambda d: self.driver.execute_script(GenericObjects.JS_GET_COMPUTED_STYLE_BY_CSS_CLASS,
                                                   color_btn) != initial_color)
        changed_color = self.driver.execute_script(GenericObjects.JS_GET_COMPUTED_STYLE_BY_CSS_CLASS, color_btn)
        print("Button color changed from", initial_color, "to", changed_color)
        # Assert that the color has changed
        assert color_btn.value_of_css_property("color") != initial_color, "Button color did not change."