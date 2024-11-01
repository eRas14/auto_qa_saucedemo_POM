from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class SearchToPage:
    def __init__(self, driver = WebDriver) -> None:
        self.driver = driver

    def search_element(self, locator: str) -> WebElement:
        """locator(str): Осуществляется поиск по локатору"""
        self.locator = locator
        return self.driver.find_element(By.CSS_SELECTOR, locator)
    
    def search_elements(self, locator: str) -> list[WebElement]:
        """locator(str): Осуществляется поиск по локатору, возвращает список"""
        self.locator = locator
        return self.driver.find_elements(By.CSS_SELECTOR, locator)