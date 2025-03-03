import pytest
from pages.dynamic_properties_page import DynamicPropertiesPage


class DynamicPropertiesTestClass:
    @pytest.mark.dynamic_properties
    def test_wait_for_buttons_visibility(self, driver):
        """
        Test Case: Navigate to Elements > Dynamic Properties and verify below scenarios
	    1 Fluently wait for button with text “Visible after 5 seconds” to be displayed
	    2 Refresh the page and verify that the second button changes color after some time
        :param driver:
        """
        dynamic_properties = DynamicPropertiesPage(driver)
        dynamic_properties.navigate()
        dynamic_properties.wait_for_elements_visibility()
