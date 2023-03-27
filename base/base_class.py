import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    def current_url(self):
        return self.driver.current_url

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result

    def assert_url(self, result):
        assert self.driver.current_url == result

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:/Users/vadko/Test/selenium_python_course/screen/' + name_screenshot)