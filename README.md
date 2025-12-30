# 10ELENA-PROJECT

conftest.py

  	  import pytest
    	from selenium import webdriver
	
    	@pytest.fixture()
    	def driver():
	    driver = webdriver.Chrome('C:/skillfactory/chromedriver.exe')
	    driver.implicitly_wait(5)
	    yield driver
	
       driver.quit()


‎pages/base_page.py‎

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Загрузка страницы
    def load(self):
        self.driver.get('https://b2c.passport.rt.ru')

    # Проверка загрузки элемента
    def is_loaded(self,locator, time=5) -> bool:
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located((locator)))
            return True
        except:
            return False

    # Найти элемент и кликнуть по нему
    def find_element_and_click(self, locator, time=5):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).click()

    # Ввод данных
    def data_input(self, locator, text, time=5):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).send_keys(text)

    # Получить атрибут текст элемента
    def get_text_of_element(self, locator, time=5):
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return element.text


pages/main_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://b2c.passport.rt.ru/')

    AUTORIZATION = (By.XPATH, "//h1[contains(text(),'Авторизация')]")
    LOGIN = (By.XPATH, "//div[@id='t-btn-tab-login']")
    USERNAME = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    BUTTON = (By.XPATH, "//button[@id='kc-login']")
    BUTTON_LOGOUT = (By.CSS_SELECTOR, "#logout-btn")
    ERROR = (By.XPATH, "//span[@id='form-error-message']")


test_rostelecom.py

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

