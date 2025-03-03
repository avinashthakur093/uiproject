import pytest
from utils.driver_setup import setup_driver
from utils.logger import logger

def pytest_addoption(parser):
    """Adds command-line option to select browser"""
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"], help="Choose browser"
                                                                                                        ": chrome or "
                                                                                                        "firefox")

@pytest.fixture(scope="function")
def driver(request):
    """Fixture to initialize WebDriver with selected browser."""
    browser = request.config.getoption("--browser")
    yield from setup_driver(browser)

@pytest.fixture(autouse=True)
def log_test_name(request):
    """Automatically logs the test function name before execution."""
    test_name = request.node.name
    logger.info(f"Starting Test: {test_name}")
    yield  # Run the test
    logger.info(f"Completed Test: {test_name}")