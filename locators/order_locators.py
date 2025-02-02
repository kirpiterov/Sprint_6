from selenium.webdriver.common.by import By
from data import TestData


class OrderLocators():
        #элементы формы "Для кого самокат"
    INPUT_NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    INPUT_SURNAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    INPUT_ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    INPUT_METRO = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    LIST_METRO_1ST_POSITION = [By.XPATH, "//ul[@class='select-search__options']//li[1]"]
    INPUT_PHONE = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    BUTTON_NEXT = [By.XPATH, "//button[text()='Далее']"]

        #элементы формы "Про аренду"
    INPUT_DELIVERY_DATE = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    CALENDAR_DATE = [
        [By.XPATH, f'//div[contains(@class,"react-datepicker__day--0{TestData.delivery_day_today}")]'],
        [By.XPATH, f'//div[contains(@class,"react-datepicker__day--0{TestData.delivery_day_tomorrow}")]']
    ]

    FIELD_RENT_LIMIT = [By.XPATH, "//div[@class='Dropdown-placeholder']"]
    DROPDOWN_RENT_1st_POSITION = [By.XPATH, "(//div[@class='Dropdown-option'])[1]"]

    RENTAL_PERIOD = [
        [By.XPATH, "(//div[@class='Dropdown-option'])[1]"],
        [By.XPATH, "(//div[@class='Dropdown-option'])[2]"]
    ]

    INPUT_CHECKBOX_COLOR = [By.XPATH, "//input[@id='black']"]
    INPUT_COMMENT_FOR_COURIER = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    BUTTON_ORDER = [By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']"]
        # элементы формы подтверждения заказа
    BUTTON_YES = [By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[text()='Да']"]
        #элементы формы "Заказ оформлен"
    BUTTON_LOOK_STATUS = [By.XPATH, "//div[contains(@class,'Order_NextButton')]/button[text()='Посмотреть статус']"]