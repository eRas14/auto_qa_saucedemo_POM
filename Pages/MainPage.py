from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_page(self, url: str):
        """"url(str): Осуществляется переход на страницу. http:www.yes,ru"""
        self.driver.get(url)
    
