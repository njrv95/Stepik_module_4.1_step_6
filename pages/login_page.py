from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login is not present in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not appears"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not appears"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field_1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_1)
        password_field_1.send_keys(password)
        password_field_2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_2)
        password_field_2.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()

#generate new email and password then return them
    def generation_email_and_password(self):
        email = str(time.time()) + "fake@gmail.com"
        password = str(time.time()) + "password"
        return email, password
