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
