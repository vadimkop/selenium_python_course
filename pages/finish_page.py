from base.base_class import Base


class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def finish(self):
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
        self.get_screenshot()

