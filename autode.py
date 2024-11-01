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

main.get_page("https://www.saucedemo.com/")

#autorization
search_to_page.search_element("#user-name").send_keys("standard_user")
search_to_page.search_element("#password").send_keys("secret_sauce")
search_to_page.search_element("#login-button").click()

items_list = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]

all_items_in_page = search_to_page.search_elements(".inventory_item_description")

print(all_items_in_page[0].text)

#add items to корзина
for i in range (len(all_items_in_page)):
    if all_items_in_page[i].find_element(By.CSS_SELECTOR, ".inventory_item_name").text in items_list:
        all_items_in_page[i].find_element(By.CSS_SELECTOR, ".btn").click()
        

search_to_page.search_element(".shopping_cart_link").click() #Press Corzina
search_to_page.search_element("#checkout").click() # Press Checkout

#input user_info
search_to_page.search_element("#first-name").send_keys("Albert")
search_to_page.search_element("#last-name").send_keys("Urazov")
search_to_page.search_element("#postal-code").send_keys("460048")

#Press continue
search_to_page.search_element("#continue").click()

#take total cost
total_cost = search_to_page.search_element(".summary_total_label").text

manager.quit_browser()

print(total_cost)