from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class DriverManager:
    def __init__(self) -> None:
        pass
        
    def get_browser(self, browser_name = "firefox") -> WebDriver:
        if browser_name.startswith("f"):
            self.driver = webdriver.Firefox()
            return self.driver
        elif browser_name.startswith("c"):
            self.driver = webdriver.Chrome()
        else:
            print("Unknow browser_name")

    def configurate(self, wait_time=4):
        """"wait_tme (int):Установка времени ожидания, по умолчанию 4сек, """
        self.driver.implicitly_wait(wait_time)
    

    def quit_browser(self) -> None:
        """"Закртиые браузера"""
        self.driver.quit()