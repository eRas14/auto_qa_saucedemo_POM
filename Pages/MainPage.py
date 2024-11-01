from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from Pages.SearchPage import SearchToPage

class MainPage(SearchToPage):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_page(self, url: str):
        """"url(str): Осуществляется переход на страницу. http:www.yes,ru"""
        self.driver.get(url)

    def autorization(self, login:str, password:str):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(login)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    
    def go_to_cart(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

    def add_user_info(self, first_name:str, last_name:str, postal_code:str):
        SearchToPage.search_element(self, "#first-name").send_keys(first_name)
        SearchToPage.search_element(self, "#last-name").send_keys(last_name)
        SearchToPage.search_element(self, "#postal-code").send_keys(postal_code)

    def click_checkout(self):
        SearchToPage.search_element(self, "#checkout").click()

    def click_continue(self):
        SearchToPage.search_element(self, "#continue").click()
