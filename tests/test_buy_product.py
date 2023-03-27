import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage


@pytest.mark.run(order=3)
def test_buy_first_product(driver, set_up):
    login = LoginPage(driver)
    login.authorization()

    main = MainPage(driver)
    main.add_first_product()

    cart = CartPage(driver)
    cart.product_confirmation()

    checkout = CheckoutPage(driver)
    checkout.input_client_info()

    payment = PaymentPage(driver)
    payment.payment()

    finish = FinishPage(driver)
    finish.finish()


@pytest.mark.run(order=1)
def test_buy_second_product(driver, set_up):
    login = LoginPage(driver)
    login.authorization()

    main = MainPage(driver)
    main.add_second_product()

    cart = CartPage(driver)
    cart.product_confirmation()


@pytest.mark.run(order=2)
def test_buy_third_product(driver, set_up):
    login = LoginPage(driver)
    login.authorization()

    main = MainPage(driver)
    main.add_third_product()

    cart = CartPage(driver)
    cart.product_confirmation()