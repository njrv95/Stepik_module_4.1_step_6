from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_IS_CLEAR_TEXT = (By.XPATH, "//*[@id='content_inner']/p")
    BASKET_ITEMS = (By.XPATH,"//div[@class='basket-items']")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.XPATH, "//input[@name ='registration-email']")
    PASSWORD_FIELD_1 = (By.XPATH, "//input[@name ='registration-password1']")
    PASSWORD_FIELD_2 = (By.XPATH, "//input[@name ='registration-password2']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    ALERT_ADDED_TO_CART = (By.XPATH, "//div[@class = 'alert alert-safe alert-noicon alert-success  fade in'][1]")
    ALERT_CART_PRICE = (By.XPATH,"//div[@class = 'alert alert-safe alert-noicon alert-info  fade in']")
    PRODUCT_NAME_FROM_ALERT = (By.XPATH, "//div[@class = 'alertinner ']/strong[1]")
    PRODUCT_NAME = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.XPATH,"//*[@class='price_color']")
    PRICE_IN_CART = (By.XPATH, "//*[@class='alertinner ']/p/strong")