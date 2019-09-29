from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_alert_added_to_cart(self):
        self.is_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART)
        PRODUCT_NAME_TEXT = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        PRODUCT_NAME_FROM_ALERT_TEXT = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_ALERT).text
        assert PRODUCT_NAME_TEXT == PRODUCT_NAME_FROM_ALERT_TEXT, "Product name not equal product name from alert"

    def should_be_alert_with_cart_price(self):
        self.is_element_present(*ProductPageLocators.ALERT_CART_PRICE)
        PRODUCT_PRICE_TEXT = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        PRICE_IN_CART_TEXT = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text
        print(PRICE_IN_CART_TEXT)
        print(PRODUCT_PRICE_TEXT)
        assert PRODUCT_PRICE_TEXT == PRICE_IN_CART_TEXT, "Product price not equal price in cart"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART), "Success message is presented, but should not be"

    def shoud_be_dissappeared(self):
        assert self.is_disappeard(*ProductPageLocators.ALERT_ADDED_TO_CART), "Success message displayed, but shoud not be"