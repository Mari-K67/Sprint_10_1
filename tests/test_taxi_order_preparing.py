import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.taxi_page_locators import TaxiPageLocators
from data import TransportDetails
#pytest tests/test_taxi_order_preparing.py

class TestTaxiOderPreparing:
    @pytest.mark.xfail(reason="Оптимальный маршрут почему-то может быть быстрее Быстрого") 
    @allure.title("смена активного таба; пересчет времени и стоимости при переключении Оптимальный\Быстрый")
    def test_optimal_fast_switching(self, driver):
        page = MainPage(driver)
        page.build_route()

        page.click(MainPageLocators.OPTIMAL)
        optimal_output_time = page.get_text(MainPageLocators.TIME_OUTPUT)
        optimal_output_price = page.get_text(MainPageLocators.PRICE_OUTPUT)

        page.click(MainPageLocators.FAST)
        fast_output_time = page.get_text(MainPageLocators.TIME_OUTPUT)
        fast_output_price = page.get_text(MainPageLocators.PRICE_OUTPUT)

        assert page.is_displayed(MainPageLocators.FAST_ACTIVE)
        assert optimal_output_time <= fast_output_time
        assert optimal_output_price != fast_output_price

    @pytest.mark.parametrize("transport_locator, transport_type", [
        (MainPageLocators.CAR, TransportDetails.CAR),
        (MainPageLocators.WALK, TransportDetails.WALK),
        (MainPageLocators.TAXI, TransportDetails.TAXI),
        (MainPageLocators.BIKE, TransportDetails.BIKE), 
        (MainPageLocators.SCOOTER, TransportDetails.SCOOTER),
        (MainPageLocators.DRIVE, TransportDetails.DRIVE)
    ])
    @allure.title("смена активного таба; активны типы передвижения  при переключении на 'Свой'")
    def test_movement_types_activity(self, driver, transport_locator, transport_type):
        page = MainPage(driver)
        page.build_route()

        page.click(MainPageLocators.OWN)
        page.click(transport_locator)
        output = page.get_text(MainPageLocators.PRICE_OUTPUT)

        assert page.is_displayed(MainPageLocators.OWN_ACTIVE)
        assert transport_type in output

    @allure.title("при выборе вида маршрута Быстрый активна кнопка Вызвать такси")
    def test_call_taxi_button_activity(self, driver):
        page = MainPage(driver)
        page.build_route()

        page.click(MainPageLocators.FAST)
        page.click(MainPageLocators.CALL_TAXI_BUTTON)

        assert page.is_displayed(TaxiPageLocators.TARIFF_BLOCK)

    @allure.title("при выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать")
    def test_call_book_button_activity(self, driver):
        page = MainPage(driver)
        page.build_route()

        page.click(MainPageLocators.OWN)
        page.click(MainPageLocators.DRIVE)
        page.click(MainPageLocators.BOOK_BUTTON)

        assert page.is_displayed(TaxiPageLocators.TARIFF_BLOCK)