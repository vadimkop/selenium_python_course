from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    first_product = "//button[@id='add-to-cart-sauce-labs-backpack']"
    second_product = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    third_product = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    menu = "//button[@id='react-burger-menu-btn']"
    about = "//a[@id='about_sidebar_link']"

    def get_first_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_product)))

    def get_second_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.second_product)))

    def get_third_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.third_product)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about)))

    def click_first_product(self):
        self.get_first_product().click()

    def click_second_product(self):
        self.get_second_product().click()

    def click_third_product(self):
        self.get_third_product().click()

    def click_cart(self):
        self.get_cart().click()

    def click_menu(self):
        self.get_menu().click()

    def click_about(self):
        self.get_about().click()

    def add_first_product(self):
        self.click_first_product()
        self.click_cart()

    def add_second_product(self):
        self.click_second_product()
        self.click_cart()

    def add_third_product(self):
        self.click_third_product()
        self.click_cart()

    def select_menu_about(self):
        self.click_menu()
        self.click_about()
        self.assert_url("https://saucelabs.com/")


