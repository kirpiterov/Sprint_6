import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать видимости элемента')
    def wait_for_element_visible(self, locator, timeout=15):
        return WDW(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать кликабельности элемента')
    def wait_for_element_clickable(self, locator, timeout=15):
        return WDW(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Кликнуть на элемент')
    def click_element(self, locator,timeout=15):
        element = self.wait_for_element_clickable(locator,timeout)
        element.click()

    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element_clickable(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_of_element(self, locator, timeout=10):
        element = self.wait_for_element_visible(locator, timeout)
        return element.text

    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element_visible(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключиться на последнюю открытую вкладку')
    def switch_to_last_opend_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        return tabs

    @allure.step('Проверить соответствие url')
    def check_current_url(self, locator, timeout=10):
        return WDW(self.driver, timeout).until(EC.url_contains(locator))