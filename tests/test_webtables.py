import pytest
from selenium.webdriver.common.by import By
from pages.webtables_page import WebTablesPage


class WebTablesTestClass:
    @pytest.mark.webtables
    def test_verify_pagination_ui(self, driver):
        """
        Test Case: Verify that the pagination controls(Next, Previous, Page Numbers) are visible
        :param driver:
        """
        previous_btn = (By.XPATH, WebTablesPage.PREVIOUS_BUTTON)
        next_btn = (By.XPATH, WebTablesPage.NEXT_BUTTON)
        page_info_element = (By.XPATH, WebTablesPage.PAGE_INFO_ELEMENT)
        page_size_combo_box = (By.XPATH, WebTablesPage.PAGE_SIZE_COMBO_BOX)
        web_tables_page = WebTablesPage(driver)
        web_tables_page.navigate()

        assert web_tables_page.element_is_visible(previous_btn) == True, ("'Previous' button is not visible on default "
                                                                          "page!")
        assert web_tables_page.element_is_visible(next_btn) == True, "'Next' button is not visible on default page!"
        assert web_tables_page.element_is_visible(page_info_element) == True, ("'Page Info element'"
                                                                               " is not visible on default page!")
        assert web_tables_page.element_is_visible(page_size_combo_box) == True, ("'Page Size Combo box is not visible "
                                                                                 "on default page!'")

    @pytest.mark.webtables
    def test_verify_default_page_load(self, driver):
        """
        Test Case: Verify when the page loads, Page 1 should be selected by default
        :param driver:
        """
        default_page = (By.XPATH, WebTablesPage.DEFAULT_PAGE)
        web_tables_page = WebTablesPage(driver)
        web_tables_page.navigate()
        assert web_tables_page.element_is_visible(default_page) == True, "Page 1 is not loaded by default!"

    def test_verify_clicking_next_button(self, driver):
        """
        Test Case: Click the 'Next' button and check if it navigates to the next page.
        :param driver:
        """
        pass

    def test_verify_clicking_previous_button(self, driver):
        """
        Test Case: Click the 'Previous' button and check if it navigates to the previous page.
        :param driver:
        """
        pass

    def test_verify_previous_button_is_disabled_on_first_page(self, driver):
        """
        Test Case: Verify when the first page is loaded, then previous button is disabled.
        :param driver:
        """
        pass
