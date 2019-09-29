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
        assert PRODUCT_NAME_TEXT == PRODUCT_NAME_FROM_ALERT_TEXT, "Product name not equal prodoct name from alert"
        print(PRODUCT_NAME_TEXT)
        print(PRODUCT_NAME_FROM_ALERT_TEXT)

    #def should_be_alert_with_cart_price(self):
        #self.is_element_present(*ProductPageLocators.ALERT_CART_PRICE)
