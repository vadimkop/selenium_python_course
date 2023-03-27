from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    user_name = "//input[@data-test='username']"
    password = "//input[@placeholder='Password']"
    login_button = "//input[@value='Login']"
    main_word = "//span[@class='title']"

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)

    def input_password(self, password):
        self.get_password().send_keys(password)

    def click_login_button(self):
        self.get_button_login().click()

    def authorization(self):
        Logger.add_start_step(method="authorization")
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Products")
        Logger.add_end_step(url=self.current_url(), method="authorization")

