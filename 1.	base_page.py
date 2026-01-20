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
