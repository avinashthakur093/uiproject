# UI Automation Framework (Selenium + Pytest)

## 📌 Project Overview
This project is a **Selenium-based UI automation framework** using **Python & Pytest**. It follows the **Page Object Model (POM)** design pattern to improve test maintainability and reusability.

---

## 🏗️ Project Structure
```
/uiproject
│-- config.py               # Configuration settings (URLs, timeouts, etc.)
│-- conftest.py             # Pytest fixtures and setup hooks
│-- pytest.ini              # Pytest configuration file
│-- requirements.txt        # List of dependencies
│
├── pages/                  # Page Object Model (POM) implementation
│   ├── base_page.py        # Common methods for all pages
│   ├── bookstore_app_page.py  # Page class for Book Store interactions
│   ├── checkbox_page.py    # Page class for Checkbox interactions
│   ├── dynamic_properties_page.py   # Page class for Dynamic Properties interactions
│   ├── elements_page.py    # Page class for Elements interactions
│   ├── home_page.py        # Page class for Landing Page.
│   ├── webtables_page.py   # Page class for Web Table interactions
│
├── tests/                  # Test cases
│   ├── test_bookstore.py   # Tests related to Book Store functionality
│   ├── test_checkboxes.py  # Tests related to Checkbox functionality
│   ├── test_dynamic_properties.py  # Tests related to Dynamic Properties functionality
│   ├── test_webtables.py   # Tests related to Web Tables functionality
│
└── utils/                  # Helper functions
    ├── driver_setup.py     # WebDriver setup and management
    ├── logger.py           # Custom logging utility
```

---

## ⚙️ Setup & Installation
### 1️⃣ Install Python (if not installed)
Ensure you have **Python 3.8+** installed. You can check your version with:
```bash
python --version
```

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate on macOS/Linux
venv\Scripts\activate  # Activate on Windows
```

### 3️⃣ Install Dependencies
Run the following command to install required packages:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Tests
### 1️⃣ Run All Tests
```bash
cd uiproject
pytest ./tests --html=report.html --self-contained-html
```
This will generate an **HTML test report**.

### 2️⃣ Run Tests in Parallel
To execute tests faster, use `pytest-xdist` to run tests in parallel:
```bash
cd uiproject
pytest -n 4 --html=report.html --self-contained-html
```
(`-n 4` runs 4 tests in parallel.)

### 3️⃣ Run Tests by Marker
To run specific test categories (e.g., `checkbox` `webtables` `dynamic_properties` `book_store_app`):
```bash
cd uiproject
pytest -m checkbox
```

---

## 📊 Test Reporting
- **HTML Report**: `report.html` will be generated after execution.
- **Logging**: Logs will be captured in `logs/test_execution.log`.

---

## 🔧 Scope for Enhancements
✅ Implement **WebDriver Manager** to remove the need for manual driver setup.

✅ Add support for multiple browsers, currently chrome and firefox supported.

✅ Improve **logging** for better debugging and tracking test failures in case of parallel execution.

✅ Add support for running automation in headless mode

✅ Add more testcases for Pagination feature

✅ Add Exception handling for handling failures gracefully

✅ Add **screenshot capture on failure** for better debugging.

✅ Extend **test coverage** for more UI interactions.

✅ Integrate with **CI/CD pipelines** (Jenkins, GitHub Actions, etc.).

---

## 🔗 References
- [Selenium Docs](https://www.selenium.dev/documentation/)
- [Pytest Docs](https://docs.pytest.org/en/latest/)
- [Python Docs](https://docs.python.org/3/)

🚀 **Thank You** 🎯

