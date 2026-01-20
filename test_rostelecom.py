from pages.main_page import MainPage
from time import sleep

# Проверка загрузки страницы авторизации
def test_main(driver):
    main_page = MainPage(driver)
    autorization = main_page.is_loaded(MainPage.AUTORIZATION)
    assert autorization == True

# Проверка кликабельности кнопки "Логин"
def test_login_is_clicable(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.LOGIN)
    login_button = main_page.is_loaded(MainPage.USERNAME)
    assert login_button == True

# Проверка позитивного сценария авторизации по почте
def test_valid_data_mail(driver):
    main_page = MainPage(driver)
    main_page.data_input(MainPage.USERNAME, "e.plechanova@mail.ru")
    main_page.data_input(MainPage.PASSWORD, "12141618Nk")
    sleep(10)
    main_page.find_element_and_click(MainPage.BUTTON)
    element = main_page.is_loaded(MainPage.BUTTON_LOGOUT)
    assert element == True

# Проверка авторизации c неправильным паролем
def test_invalid_data(driver):
    main_page = MainPage(driver)
    main_page.data_input(MainPage.USERNAME, "e.plechanova@mail.ru")
    main_page.data_input(MainPage.PASSWORD, "121416Nk")
    main_page.find_element_and_click(MainPage.BUTTON)
    error_button = main_page.is_loaded(MainPage.ERROR)
    assert error_button == True
