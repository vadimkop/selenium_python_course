from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CheckoutPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)

    def click_continue_button(self):
        self.get_continue_button().click()

    def input_client_info(self):
        self.input_first_name("Polar")
        self.input_last_name("Orca")
        self.input_postal_code("31")
        self.click_continue_button()

