import abc


class BasePage(abc.ABC):
    """An abstract base class used for navigation from https://demoqa.com to specific pages"""

    def __init__(self, driver):
        self.driver = driver

    @abc.abstractmethod
    def navigate(self):
        """
        Abstract function, to be used for navigation from demoqa homepage to different pages.
        """
        pass
