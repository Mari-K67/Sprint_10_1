import allure
from data import Adress
from locators.main_page_locators import MainPageLocators
from locators.taxi_page_locators import TaxiPageLocators
from pages.base_page import BasePage

class TaxiPage(BasePage):
    allure.step('''
        1. заполнить поля "Откуда" и "Куда";
        2. выбрать вид маршрута Быстрый;
        3. нажать кнопку Вызвать такси
    ''')
    def go_to_taxi_page(self):
        self.send_keys(MainPageLocators.FROM_FIELD, Adress.ADRESS_1)
        self.send_keys(MainPageLocators.WHERE_FIELD, Adress.ADRESS_2)
        self.click(MainPageLocators.FAST)
        self.click(MainPageLocators.CALL_TAXI_BUTTON)

    allure.step('''
        1. заполнить поля "Откуда" и "Куда";
        2. выбрать вид маршрута Быстрый;
        3. нажать кнопку Вызвать такси;
        4. выбирать тариф Рабочий;
        5. включить чекбокс Столик для ноутбука;
        6. нажать кнопку Ввести номер и заказать
    ''')
    def go_to_car_search_page(self):
        self.go_to_taxi_page()
        self.click(TaxiPageLocators.WORK_TARIFF)
        self.click(TaxiPageLocators.REQUIREMENTS_BUTTON)
        self.click(TaxiPageLocators.CHECK_BOX)
        self.click(TaxiPageLocators.MAKE_ODER_BUTTON)

    allure.step('''
        1. заполнить поля "Откуда" и "Куда";
        2. выбрать вид маршрута Быстрый;
        3. нажать кнопку Вызвать такси;
        4. выбирать тариф Рабочий;
        5. включить чекбокс Столик для ноутбука;
        6. нажать кнопку Ввести номер и заказать;
        7. дождаться окончания таймера поиска машины
    ''')
    def go_to_completed_order_page(self):
        self.go_to_car_search_page()
        self.wait_element_visability(TaxiPageLocators.COMPLETED_ODER_TITLE)