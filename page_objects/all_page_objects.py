class GenericObjects:
    SCROLL_INTO_VIEW = "arguments[0].scrollIntoView(true);"
    JS_GET_COMPUTED_STYLE_BY_CSS_CLASS = "return window.getComputedStyle(arguments[0]).color;"

    def __init__(self):
        raise TypeError("This class should not be instantiated")


class HomePageObjects:
    ELEMENTS_LINK = "//h5[text()='Elements']"

    def __init__(self):
        raise TypeError("This class should not be instantiated")


class ElementsPageObjects:
    CHECKBOX_LINK = "//span[text()='Check Box']"
    WEB_TABLES_LINK = "//span[text()='Web Tables']"
    DYNAMIC_PROPERTIES_LINK = "//span[text()='Dynamic Properties']"
    BOOK_STORE_APP_LINK = "//div[text()='Book Store Application']"
    BOOK_STORE_LINK = "//span[text()='Book Store']"

    def __init__(self):
        raise TypeError("This class should not be instantiated")


class CheckboxPageObjects:
    EXPAND_BUTTONS = "//button[contains(@class, 'rct-collapse')]"
    EXPAND_ALL_BUTTONS = "//button[@title='Expand all']//*[name()='svg']"
    EXPAND_ALL_BUTTON = "button[title='Expand all']"
    CHECKBOX_TOGGLE_BUTTONS = "button[aria-label='Toggle']"
    HOME_CHECKBOX = "(//*[name()='svg'][@class='rct-icon rct-icon-expand-close'])"
    CHECKBOX_SHRINKED = "(//*[name()='svg'][@class='rct-icon rct-icon-expand-close'])"
    SELECTED_CHECKBOX = ".//*[local-name()='svg']"
    SELECTED_CHECKBOX_TEXT = "'./following-sibling::span[@class=\'rct-title\']'"
    HOME_CHECKBOX_PARTIAL_CHECK_XPATH = "label[for='tree-node-home'] span[class='rct-checkbox'] svg path"
    DOCUMENTS_CHECKBOX_PARTIAL_CHECK_XPATH = "label[for='tree-node-documents'] span[class='rct-checkbox'] svg path"
    OFFICE_CHECKBOX_PARTIAL_CHECK_XPATH = "label[for='tree-node-office'] span[class='rct-checkbox'] svg path"
    PRIVATE_CHECKBOX_XPATH = "//span[contains(text(),'Private')]"
    CHECKED_PRIVATE_CHECKBOX_XPATH = "(//*[name()='svg'][@class='rct-icon rct-icon-check'])[1]"

    def __init__(self):
        raise TypeError("This class should not be instantiated")


class WebTablesPageObjects:
    ADD_ROW_BUTTON = "//button[@id='addNewRecordButton']"
    FIRST_NAME = "//input[@id='firstName']"
    LAST_NAME = "//input[@id='lastName']"
    EMAIL = "//input[@id='userEmail']"
    AGE = "//input[@id='age']"
    SALARY = "//input[@id='salary']"
    DEPARTMENT = "//input[@id='department']"
    SUBMIT_BUTTON = "//button[@id='submit']"
    PREVIOUS_BUTTON = "//button[contains(text(), 'Previous')]"
    NEXT_BUTTON = "//button[contains(text(), 'Next')]"
    PAGE_INFO_ELEMENT = "//span[@class='-pageInfo']"
    PAGE_SIZE_COMBO_BOX = "//span[@class='select-wrap -pageSizeOptions']"
    DEFAULT_PAGE = "//input[@aria-label='jump to page' and @value='1']"

    def __init__(self):
        raise TypeError("This class should not be instantiated")


class DynamicPropertiesPageObjects:
    ENABLE_AFTER_5S_BTN = "//button[@id='enableAfter']"
    COLOR_CHANGE_BTN = "//button[@id='colorChange']"
    VISIBLE_AFTER_5S_BTN = "//button[@id='visibleAfter']"

    def __init__(self):
        raise TypeError("This class should not be instantiated")


class BookStorePageObjects:
    BOOK_LIST_TABLE_BODY = "rt-tbody"
    ALL_BOOK_LIST = "rt-tr-group"
    BOOK_TITLE = "mr-2"
    BOOK_AUTHOR_PUBLISHER = "rt-td"

    def __init__(self):
        raise TypeError("This class should not be instantiated")
