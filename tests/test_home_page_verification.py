import pytest
from ctreport_selenium.ctlistener import Test
from pages.homepage import HomePage
from pages.productspage import ProductPage
from testdata.getdata import get_data
# from testdata.read_from_excel import get_data


class TestHomePageVerification:
    driver = None
    test = None

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setupclass(cls, getdriver):
        TestHomePageVerification.driver = getdriver

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("data", get_data("Android Test Data.xlsx", "Test Data"))
    def test_home_page_verification(self, data):
        self.test = Test("Home Page Verification Test for GS",
                         description="Home Page and Navigate to Product Page Vrification Test")

        self.test.log("Home Page Verification Test Started")

        home_page = HomePage(self.driver)

        home_page.enter_name(data["Name"])

        self.test.log("User sucessfully entered the name field")

        home_page.click_lets_shop_button()

        self.test.log("User sucessfully clicked the lets shop button")

        actual_data = home_page.verify_products_page()

        expected_data = "Products"

        self.test.assert_are_equal(actual_data, expected_data, description="Sucessfully Navigate to Product Page",
                                   onfail_screenshot=False)

        self.test.log("Home Page Verification Test Ended")

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("data", get_data("Android Test Data.xlsx", "Test Data"))
    def test_product_page_verification(self, data):
        self.test = Test("Product Page Verification Test for GS",
                         description="Product Page and Navigate to Checkout Page Vrification Test")

        self.test.log("Product Page Verification Test Started")

        product_page = ProductPage(self.driver)

        first_product_name = product_page.find_first_product()

        self.test.log("First Product visible in the Product Page")

        product_page.add_first_product()

        self.test.log("First Product add to cart sucessfully")

        product_page.click_cart_button()

        self.test.log("Cart open sucessfully")

        added_product_name = product_page.added_product_name()

        self.test.assert_are_equal(first_product_name, added_product_name, description="First Product Added Correctly",
                                   onfail_screenshot=False)

        self.test.log("Product Page Verification Test Ended")

    def teardown_method(self, method):
        TestHomePageVerification.test = self.test
