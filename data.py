import datetime


today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

class TestData:
    base_url = 'https://qa-scooter.praktikum-services.ru/'
    dzen_redirect_url = 'https://dzen.ru/?yredirect=true'

        #для параметризации локаторов текущей и следующей даты
    delivery_day_today = today.strftime('%d')
    delivery_day_tomorrow = tomorrow.strftime('%d')
