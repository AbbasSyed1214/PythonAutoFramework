from playwright.sync_api import Page, expect

class IphonePage:

    search_field = "xpath=//input[@id='desktop-searchbar']"
    iphone_version = "xpath=//img[@alt='<<Replace_Text>>']"
    condition = "xpath=//li//div[@class='w-full']//span[contains(text(),'<<Replace_Text>>')]"
    cart_btn = "xpath=//span[contains(text(),'Go to cart')]"
    sum_prices = None
    total = None


    def __init__(self, page):
        self.page = page
        self.page.goto("https://www.backmarket.co.uk/")
        self.page.get_by_role("button", name="I'm cool with that").click()

    def search(self, text):
        self.page.locator(self.search_field).fill(text)
        self.page.get_by_role("searchbox", name="Try iPhone 11, MacBook, AirPods...").press("Enter")

    def select_iphone(self, iphone_version):
        self.page.locator(self.iphone_version.replace("<<Replace_Text>>", iphone_version)).click()

    def select_condition(self, pstr_condition):
        self.page.locator(self.condition.replace("<<Replace_Text>>", pstr_condition)).click()

    def click_buy_button(self):
        self.page.get_by_role("button", name="Buy").click()

    def verify_cart_items(self, text):
        return True if text in self.page.content() else False

    def goto_cart(self):
        self.page.locator(self.cart_btn).click()

    def select_damage_cover(self, damage_option):
        self.page.get_by_text(damage_option).click()

    def get_all_prices_in_summary(self):

        prices = self.page.query_selector_all('[data-qa="price"]').inner_text()
        self.total = self.page.query_selector('[data-qa="price-after-discount"]').inner_text()

        prices = [float(price.replace('£', '').replace(',', '').strip()) for price in prices]
        self.total = float(self.total.replace('£', '').replace(',', '').strip())

        self.sum_prices = sum(prices)

    def verify_sum_of_prices(self):
        self.get_all_prices_in_summary()
        return self.prices == self.total