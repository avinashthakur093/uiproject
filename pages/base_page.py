from abc import ABC, abstractmethod

class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def navigate(self):
        pass
