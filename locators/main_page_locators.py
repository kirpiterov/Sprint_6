from selenium.webdriver.common.by import By


class MainPageLocators():
        # эти ссылки присутствуют на всех экранах
    LINK_LOGO_YANDEX = [By.XPATH, "//a/img[@alt='Yandex']"]
    LINK_LOGO_SCOOTER = [By.XPATH, "//a/img[@alt='Scooter']"]    #должна вести на base_url
        #верхняя и нижняя кнопки Заказать
    BUTTON_ORDER = [
        [By.XPATH, "//div[contains(@class,'Header')]/button[text()='Заказать']"],
        [By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']"]
    ]
    BUTTON_ORDER_1 = [By.XPATH, "//div[contains(@class,'Header')]/button[text()='Заказать']"]
    BUTTON_ORDER_2 = [By.XPATH, "//div[contains(@class,'Home')]/button[text()='Заказать']"]

    BUTTON_COOKIE_CONFIRM = [By.XPATH, "//button[@id='rcc-confirm-button']"]
    FAQ_PANEL = [By.XPATH, "//div[@class='accordion']"]

    @staticmethod
    def question_number(number):
        return By.XPATH, f'//div[@id="accordion__heading-{number}"]'

    @staticmethod
    def answer_locator(number):
        return By.XPATH, f'//div[@id="accordion__panel-{number}"]'
