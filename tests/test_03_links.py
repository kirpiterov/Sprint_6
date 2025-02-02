import allure
from data import TestData
from pages.main_page import MainPage


class TestLinksFromOrderPage():
    @allure.title('Тест перехода со страницы заказа на сайт Самоката по клику на логотип')
    def test_from_logo_to_page_Scooter(self,driver):
        main_page = MainPage(driver)
        main_page.click_order_button()
        main_page.click_logo_Scooter()

        assert driver.current_url == TestData.base_url

    @allure.title('Тест перехода со страницы заказа на сайт Дзен по клику на логотип')
    def test_from_logo_to_page_Yandex(self,driver):
        main_page = MainPage(driver)
        main_page.click_order_button()
        main_page.click_logo_Yandex()

        assert driver.current_url == TestData.dzen_redirect_url

