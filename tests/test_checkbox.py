import pytest
import random
from utils.logger import logger
from pages.checkbox_page import CheckboxPage


class DemoqaCheckboxTestClass:
    @pytest.mark.checkbox
    def test_expand_all_checkboxes(self, driver):
        """
        Test Case: Navigate to Elements > Checkbox, Dynamically expand the tree at all levels
        :param driver:
        :return:
        """
        checkbox_page = CheckboxPage(driver)
        checkbox_page.navigate()
        status = checkbox_page.expand_checkbox()
        logger.info(f"Test status: {status}")
        assert status == True, "Test Failed, Some Checkboxes are not expanded!"

    @pytest.mark.checkbox
    def test_check_level2_checkbox_recursively(self, driver):
        """
        Test Case: Navigate to Elements > Checkbox, Tick a parent node and dynamically assert all
        nested elements have correct icons
        :param driver:
        :return:
        """
        checkbox_page = CheckboxPage(driver)
        checkbox_page.navigate()
        checkbox_page.expand_checkbox()
        level2_check_box_superset = ["Desktop", "Documents", "Downloads"]
        # Randomly passing the level 2 checkbox label to select
        # And assert that checkbox, and it's child node is selected
        checkbox_page.expand_level2_checkbox(random.choice(level2_check_box_superset))

    @pytest.mark.checkbox
    def test_check_specific_checkbox(self, driver):
        """
        Test Case: Navigate to Elements > Checkbox
        Tick “Home > Documents > Office > Private” and assert that the correct icons are displayed
        nested elements have correct icons
        :param driver:
        :return:
        """
        checkbox_page = CheckboxPage(driver)
        checkbox_page.navigate()
        checkbox_page.expand_checkbox()
        assert checkbox_page.expand_private_checkbox() == True, ("Home > Documents > Office > Private checkbox is "
                                                                 "selected")
