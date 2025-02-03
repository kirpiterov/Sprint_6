import allure

from data import TestData
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем первую кнопку "Заказать"')
    def click_order_button(self):
        self.click_element(MainPageLocators.BUTTON_ORDER[0])

    @allure.step('Кликаем на логотип "Самокат"')
    def click_logo_Scooter(self):
        self.click_element(MainPageLocators.LINK_LOGO_SCOOTER)

    @allure.step('Кликаем на логотип "Яндекс"')
    def click_logo_Yandex(self):
        self.click_element(MainPageLocators.LINK_LOGO_YANDEX)
        self.switch_to_last_opend_tab()
        self.check_current_url(TestData.dzen_redirect_url)

    @allure.step('Кликаем на кнопку подтверждения кук')
    def click_cookie_confirm(self):
        self.click_element(MainPageLocators.BUTTON_COOKIE_CONFIRM)

    @allure.step('Дожидаемся доступности панели вопросов')
    def wait_faq_panel_visibility(self):
        self.wait_for_element_visible(MainPageLocators.FAQ_PANEL)
        self.scroll_to_element(MainPageLocators.FAQ_PANEL)

    @allure.step('Кликаем на вопрос и возвращаем текст ответа')
    def click_to_question(self,question_number):
        question_locator = MainPageLocators.question_number(question_number)
        answer_locator = MainPageLocators.answer_locator(question_number)
        self.wait_for_element_clickable(question_locator)
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
        self.wait_for_element_visible(answer_locator)
        self.scroll_to_element(answer_locator)
        actual_text = self.get_text_of_element(answer_locator)
        return actual_text

    @allure.step('Проверяем, что текущая страница - главная')
    def check_current_page_is_main(self):
        return self.check_current_url(TestData.base_url)

    @allure.step('Проверяем, что текущая страница - редирект на Дзен')
    def check_current_page_is_dzen_redirect(self):
        return self.check_current_url(TestData.dzen_redirect_url)

