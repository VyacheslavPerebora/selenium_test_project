from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_log = LoginPage(browser, browser.current_url)
    page_log.should_be_login_url()


def test_should_be_logform(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_log = LoginPage(browser, browser.current_url)
    page_log.should_be_login_form()


def test_should_be_regform(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_log = LoginPage(browser, browser.current_url)
    page_log.should_be_register_form()
