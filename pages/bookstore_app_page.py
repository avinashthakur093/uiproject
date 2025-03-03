from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.all_page_objects import BookStorePageObjects
from pages.base_page import BasePage
from pages.elements_page import ElementsPage
from utils.logger import logger
from config import Config


class BookStorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate(self):
        """
        Function navigates to Book Store Application Page
        """
        elements_page = ElementsPage(self.driver)
        elements_page.navigate()
        elements_page.click_book_store_application()
    def get_books_info(self):
        """
        Function to fetch all the books info(title, author and publisher) displayed in UI
        :return:
        """
        # Wait until the book list is visible
        wait = WebDriverWait(self.driver, Config.shortTimeout)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, BookStorePageObjects.BOOK_LIST_TABLE_BODY)))

        # Fetch all books information
        books = self.driver.find_elements(By.CLASS_NAME, BookStorePageObjects.ALL_BOOK_LIST)
        book_info_list = []
        count = 0
        for book in range(0, 8):
            title = books[book].find_element(By.CLASS_NAME, BookStorePageObjects.BOOK_TITLE).text
            # Assuming 2nd column is author
            author = books[book].find_elements(By.CLASS_NAME, BookStorePageObjects.BOOK_AUTHOR_PUBLISHER)[1].text
            # Assuming 3rd column is publisher
            publisher = books[book].find_elements(By.CLASS_NAME, BookStorePageObjects.BOOK_AUTHOR_PUBLISHER)[2].text
            count += 1
            book_info_list.append({"title": title, "author": author, "publisher": publisher})
        return book_info_list

    def compare_books_info(self, books_data_ui, books_data_api):
        """
        Function to compare books info fetched from UI and API
        :param books_data_ui: Data fetched from UI
        :param books_data_api: Data fetched from API
        :return: Returns True if all info matches, else false
        """
        errors = []
        for ui_book, api_book in zip(books_data_ui, books_data_api):
            mismatches = {}
            for key in ui_book.keys():
                if ui_book[key] != api_book[key]:
                    mismatches[key] = {'UI': ui_book[key], 'API': api_book[key]}

            if mismatches:
                errors.append({"title": ui_book['title'], "mismatches": mismatches})

        if errors:
            logger.info(f"Data mismatches found:")
            for error in errors:
                for key, value in error['mismatches'].items():
                    logger.info(f" Book: {error['title']} Mismatch in '{key}': UI='{value['UI']}', API='{value['API']}'")
            return False
        else:
            logger.info("All book details match.")
            return True
