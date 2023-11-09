from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class HomePage(BasePage):
    name_text_field = By.ID, "com.androidsample.generalstore:id/nameField"
    lets_shop_button = By.ID, "com.androidsample.generalstore:id/btnLetsShop"
    products = By.ID, "com.androidsample.generalstore:id/toolbar_title"

    def enter_name(self, name):
        self._enter_text(self.name_text_field, name)

    def click_lets_shop_button(self):
        self._wait_for_element(self.lets_shop_button, "visibility").click()

    def verify_products_page(self):
        return self._wait_for_element(self.products, "visibility").text
