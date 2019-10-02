from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_clear_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket has got items"
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_CLEAR_TEXT), "Text 'basket is empty' is not present"