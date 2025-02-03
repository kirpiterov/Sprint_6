import allure
import pytest
from pages.order_page import OrderContactPage
from datasets import TestDatasets


class TestOrder:
    @allure.title('Тест заказа самоката')
    @pytest.mark.parametrize('dataset', TestDatasets.dataset)
    def test_successfull_scooter_order(self, driver, dataset):
        order_contact_page = OrderContactPage(driver)
        order_contact_page.click_button_cookie_confirm()
        order_contact_page.click_button_order_param1(dataset)
        order_contact_page.fill_order_contacts(dataset)
        order_contact_page.fill_form_about_rent(dataset)

        #проверяем, что в открывшейся форме есть кнопка "Посмотреть статус"
        assert order_contact_page.opened_form_has_necessary_element()


