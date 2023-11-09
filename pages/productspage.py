from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class ProductPage(BasePage):
    first_product = By.XPATH, '//android.widget.TextView[@resource-id="com.androidsample.generalstore:id/productName" and @text="Air Jordan 4 Retro"]'
    add_to_cart_of_first_product = By.XPATH, '(//android.widget.TextView[@resource-id="com.androidsample.generalstore:id/productAddCart"])[1]'
    cart_button = By.ID, 'com.androidsample.generalstore:id/appbar_btn_cart'
    added_product_name_ele = By.ID, 'com.androidsample.generalstore:id/productName'

    def find_first_product(self):
        return self._wait_for_element(self.first_product, "visibility").text

    def add_first_product(self):
        self._wait_for_element(self.add_to_cart_of_first_product, "visibility").click()

    def click_cart_button(self):
        self._wait_for_element(self.cart_button, "visibility").click()

    def added_product_name(self):
        return self._wait_for_element(self.added_product_name_ele, "visibility").text
