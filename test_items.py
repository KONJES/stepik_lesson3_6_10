from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"), "Add to basket button is missing"
