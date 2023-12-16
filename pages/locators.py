from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_VIEW_ICON_IN_HEADER = (By.CSS_SELECTOR, "header>div .basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    ITEM_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_ICON_BUTTON = (By.CSS_SELECTOR, '#register_form button[type="submit"]')


class MainPageLocators:
    pass


class ProductPageLocators:
    BASKET_ICON = (By.CSS_SELECTOR, "#add_to_basket_form>button")
    ITEM_ADDED_TO_BASKET = (By.CSS_SELECTOR, '.alert-safe:nth-of-type(1) .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    BASKET_VALUE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    COST_OF_ITEM = (By.CSS_SELECTOR, 'p.price_color')




