import pytest
from pages.bookstore_app_page import BookStorePage
from utils.api_request import fetch_books
from utils.logger import logger
class BookStoreTestClass:

    @pytest.mark.book_store_app
    def test_verify_book_info(self, driver):
        """
        Test Case: Navigate to Book Store Application
	    Look at the list of books and use the api to validate the correctness of the data displayed on the book
	    store page
        :param driver:
        """
        book_store_app = BookStorePage(driver)
        book_store_app.navigate()
        books_info_from_ui = book_store_app.get_books_info()
        books_info_from_api = fetch_books()
        books_info_from_api = books_info_from_api.get('books')
        keys_to_compare = ["title", "author", "publisher"]
        updated_books_info_from_api = [{k: v for k, v in book.items() if k in keys_to_compare} for book in
                                       books_info_from_api]
        logger.info (f"=================================================")
        logger.info(f"Book info from UI: {books_info_from_ui}")
        logger.info (f"=================================================")
        logger.info(f"Book info from API updated list: {updated_books_info_from_api}")
        logger.info (f"=================================================")
        assert book_store_app.compare_books_info(books_info_from_ui, updated_books_info_from_api) == True, ("Books "
                                                                                                            "info Not "
                                                                                                            "Matching")


