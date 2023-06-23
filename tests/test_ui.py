from forms.iphone.iphone_page import IphonePage
from playwright.sync_api import Page


def test_add_iphone_128_good_condition(page: Page):
    driver = IphonePage(page)
    driver.search("Iphone 128 GB")
    driver.select_iphone("iPhone 11 128 GB - Black - Unlocked")
    driver.select_condition("Good")
    driver.click_buy_button()
    assert driver.verify_cart_items("iPhone 11 was added to cart")
    driver.goto_cart()
    driver.select_damage_cover("12-month Damage Cover • £35.88 12-month contract cover for accidental breakage a")
    assert driver.verify_sum_of_prices()