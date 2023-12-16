from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def register_new_user(self, email: str, password: str):
        em = self.browser.find_element(By.CSS_SELECTOR, "#register_form #id_registration-email")
        em.send_keys(email)
        pas1 = self.browser.find_element(By.CSS_SELECTOR, "#register_form #id_registration-password1")
        pas1.send_keys(password)
        pas2 = self.browser.find_element(By.CSS_SELECTOR, "#register_form #id_registration-password2")
        pas2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_ICON_BUTTON)
        reg_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It's not a login_url"

    def should_be_login_form(self):
        # реализуем проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is absent"

    def should_be_register_form(self):
        # реализуем проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is absent"

