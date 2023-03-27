from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_link_about(driver, set_up):
    login = LoginPage(driver)
    login.authorization()

    main = MainPage(driver)
    main.select_menu_about()