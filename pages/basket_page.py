from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_clear_basket(self):
        self.click_basket_button()
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_CLEAR_TEXT), "Text 'basket is clear' is not present"