import allure
from pages.main_page import MainPage


class TestLinksFromOrderPage():
    @allure.title('Тест перехода со страницы заказа на сайт Самоката по клику на логотип')
    def test_from_logo_to_page_Scooter(self,driver):
        main_page = MainPage(driver)
        main_page.click_order_button()
        main_page.click_logo_Scooter()

        assert main_page.check_current_page_is_main

    @allure.title('Тест перехода со страницы заказа на сайт Дзен по клику на логотип')
    def test_from_logo_to_page_Yandex(self,driver):
        main_page = MainPage(driver)
        main_page.click_order_button()
        main_page.click_logo_Yandex()

        assert main_page.check_current_page_is_dzen_redirect

