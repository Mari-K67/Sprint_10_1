import allure
from data import Adress
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Заполнить поля "Откуда" и "Куда"')
    def build_route(self):
        self.send_keys(MainPageLocators.FROM_FIELD, Adress.ADRESS_1)
        self.send_keys(MainPageLocators.WHERE_FIELD, Adress.ADRESS_2)

    @allure.step('Заполнить поля "Откуда" и "Куда" одинаковым значением')
    def build_route_same_adress(self):
        self.send_keys(MainPageLocators.FROM_FIELD, Adress.ADRESS_1)
        self.send_keys(MainPageLocators.WHERE_FIELD, Adress.ADRESS_1)
    
    