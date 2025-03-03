import requests
from utils.logger import logger

BASE_URL = "https://demoqa.com/BookStore/v1/Books"
HEADERS = {
    "Referer": "https://demoqa.com/books",
}

def fetch_books(url=BASE_URL, headers=None):
    """Fetches book data from the DemoQA Book Store API."""
    if headers is None:
        headers = HEADERS
    logger.info(f"Invoking API: {BASE_URL}")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)
        logger.info(f"API Status Code: {response.status_code}")
        return response.json()  # Return parsed JSON response
    except requests.exceptions.RequestException as e:
        logger.info(f"Error fetching books: {e}")
        return None