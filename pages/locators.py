from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    ALERT_ADDED_TO_CART = (By.XPATH, "//div[@class = 'alert alert-safe alert-noicon alert-success  fade in'][1]")
    ALERT_CART_PRICE = (By.XPATH,"//div[@class = 'alert alert-safe alert-noicon alert-info  fade in']")
    PRODUCT_NAME_FROM_ALERT = (By.XPATH, "//div[@class = 'alertinner ']/strong[1]")
    PRODUCT_NAME = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.XPATH,"//*[@class='price_color']")
    PRICE_IN_CART = (By.XPATH, "//*[@class='alertinner ']/p/strong")