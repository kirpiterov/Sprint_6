import allure
from locators.main_page_locators import MainPageLocators
from locators.order_locators import OrderLocators
from pages.base_page import BasePage


class OrderContactPage(BasePage):
    @allure.step('Нажимаем кнопку для подтвердждения куки')
    def click_button_cookie_confirm(self):
        self.click_element(MainPageLocators.BUTTON_COOKIE_CONFIRM)

    @allure.step('Нажимаем кнопку "Заказать", переданную в параметре')
    def click_button_order_param1(self, dataset):
        self.click_element(dataset['button_order'])

    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_order_contacts(self, dataset):
        self.send_keys_to_input(OrderLocators.INPUT_NAME, dataset['name'])
        self.send_keys_to_input(OrderLocators.INPUT_SURNAME, dataset['surname'])
        self.send_keys_to_input(OrderLocators.INPUT_ADDRESS, dataset['address'])
        self.click_element(OrderLocators.INPUT_METRO)
        self.click_element(OrderLocators.LIST_METRO_1ST_POSITION)
        self.send_keys_to_input(OrderLocators.INPUT_PHONE, dataset['phone'])
        self.click_element(OrderLocators.BUTTON_NEXT)

    #После нажатия кнопки Далее открывается форма "Про аренду"
    @allure.step('Заполняем форму "Про аренду"')
    def fill_form_about_rent(self, dataset):
        self.click_element(OrderLocators.INPUT_DELIVERY_DATE)
        self.click_element(dataset['delivery_date'])
        self.click_element(OrderLocators.FIELD_RENT_LIMIT)
        self.click_element(dataset['rental_period'])
        self.click_element(OrderLocators.INPUT_CHECKBOX_COLOR)
        self.send_keys_to_input(OrderLocators.INPUT_COMMENT_FOR_COURIER, dataset['comment_for_courier'])
        self.click_element(OrderLocators.BUTTON_ORDER)
        self.click_element(OrderLocators.BUTTON_YES)

    @allure.step('Убеждаемся в наличии нужного элемента на форме')
    def opened_form_has_necessary_element(self):
        return self.wait_for_element_visible(OrderLocators.BUTTON_LOOK_STATUS)


