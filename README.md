# Данный автотест имитирует поведение пользователя на сайте интернет-магазина Saucedemo, выполнено в стиле Pages Obejct Model
## Тест включает в себя авторизацию:    
### -Авторизация пользователя
### -Добавление товаров в корзину
### -Заполнение формы для оформления заказа 


```

from Pages.DriverManager import DriverManager
from Pages.MainPage import MainPage
from Pages.SearchPage import SearchToPage
from selenium.webdriver.common.by import By


#Inizialization
manager = DriverManager()
driver = manager.get_browser("f")
main = MainPage(driver)
search_to_page = SearchToPage(driver)
manager.configurate(2)

#go to site
main.get_page("https://www.saucedemo.com/")

#autorization
main.autorization("standard_user","secret_sauce")

#add to cart
search_to_page.add_to_bag("Sauce Labs Backpack")
search_to_page.add_to_bag("Sauce Labs Bolt T-Shirt")

#cart
main.go_to_cart()

#click_checkout
main.click_checkout()

#input user_info
main.add_user_info("Albert", "Urazov", "460048")

#Press continue
main.click_continue()

manager.quit_browser()
