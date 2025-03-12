import pytest
from selenium.webdriver.common.by import By
from pages.webtables_page import WebTablesPage
from utils.logger import logger


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

    @pytest.mark.webtables
    def test_verify_previous_and_next_button_is_disabled_on_first_page(self, driver):
        """
        Test Case: Verify when the first page is loaded, then previous and next button is disabled when page count is 1.
        :param driver:
        """
        web_tables_page = WebTablesPage(driver)
        web_tables_page.navigate()
        # disabled_previous_button = driver.find_element(By.XPATH, WebTablesPage.DISABLED_PREVIOUS_BUTTON)
        disabled_previous_button = web_tables_page.find_element(By.XPATH, WebTablesPage.DISABLED_PREVIOUS_BUTTON)
        # disabled_next_button = driver.find_element(By.XPATH, WebTablesPage.DISABLED_NEXT_BUTTON)
        disabled_next_button = web_tables_page.find_element(By.XPATH, WebTablesPage.DISABLED_NEXT_BUTTON)
        assert disabled_previous_button is not None, "Previous Button is not disabled."
        assert disabled_next_button is not None, "Next Button is not disabled."

    @pytest.mark.webtables
    def test_verify_new_page_gets_added_after_adding_rows_more_than_page_size(self, driver):
        """
        Test Case: Verify when the number of records in the page is equal to the max number of records allowed in the
        page, verify if a new page gets added for an addition of new record here.
        """
        web_tables_page = WebTablesPage(driver)
        web_tables_page.navigate()
        current_page_count = web_tables_page.get_total_page_count()
        web_tables_page.add_new_rows(10)
        total_page_count = web_tables_page.get_total_page_count()
        # assert total_page_count > current_page_count and total_page_count > 0, "Page number not added"
        logger.info(f"Current Page Count: {current_page_count}, Total Page Count: {total_page_count}")
        assert 0 < total_page_count > current_page_count, ("New page not got added after adding rows more than allowed "
                                                           "page size")


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


