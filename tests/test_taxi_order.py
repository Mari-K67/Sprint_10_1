import allure
import pytest
from pages.taxi_page import TaxiPage
from locators.taxi_page_locators import TaxiPageLocators
from data import TaxiInformation
#pytest tests/test_taxi_order.py

class TestTaxiOderPreparing:
    @allure.title("открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный")
    def test_tariffs_are_displayed(self, driver):
        page = TaxiPage(driver)
        page.go_to_taxi_page()

        assert page.is_displayed(TaxiPageLocators.TARIFF_BLOCK)
        assert page.element_is_clickable(TaxiPageLocators.WORK_TARIFF)

    @pytest.mark.xfail(reason="Несоответствие орисаний по ТЗ", strict=False) 
    @pytest.mark.parametrize("tariff, i_button, title, descreption, title_expected, descreption_expected", [
        (TaxiPageLocators.WORK_TARIFF, TaxiPageLocators.I_BUTTON_WORK, TaxiPageLocators.INFO_TITLE_WORK, TaxiPageLocators.INFO_DESCRIPTION_WORK, TaxiInformation.WORK_TITLE, TaxiInformation.WORK_DESCRIPTION),
        (TaxiPageLocators.SLEEPY_TARIFF, TaxiPageLocators.I_BUTTON_SLEEPY, TaxiPageLocators.INFO_TITLE_SLEEPY, TaxiPageLocators.INFO_DESCRIPTION_SLEEPY, TaxiInformation.SLEEPY_TITLE, TaxiInformation.SLEEPY_DESCRIPTION),
        (TaxiPageLocators.VACATION_TARIFF, TaxiPageLocators.I_BUTTON_VACATION, TaxiPageLocators.INFO_TITLE_VACATION, TaxiPageLocators.INFO_DESCRIPTION_VACATION, TaxiInformation.VACATION_TITLE, TaxiInformation.VACATION_DESCRIPTION),
        (TaxiPageLocators.TALKATIVE_TARIFF, TaxiPageLocators.I_BUTTON_TALKATIVE, TaxiPageLocators.INFO_TITLE_TALKATIVE, TaxiPageLocators.INFO_DESCRIPTION_TALKATIVE, TaxiInformation.TALKATIVE_TITLE, TaxiInformation.TALKATIVE_DESCRIPTION),
        (TaxiPageLocators.COMFORTING_TARIFF, TaxiPageLocators.I_BUTTON_COMFORTING, TaxiPageLocators.INFO_TITLE_COMFORTING, TaxiPageLocators.INFO_DESCRIPTION_COMFORTING, TaxiInformation.COMFORTING_TITLE, TaxiInformation.COMFORTING_DESCRIPTION),
        (TaxiPageLocators.GLOSSY_TARIFF, TaxiPageLocators.I_BUTTON_GLOSSY, TaxiPageLocators.INFO_TITLE_GLOSSY, TaxiPageLocators.INFO_DESCRIPTION_GLOSSY, TaxiInformation.GLOSSY_TITLE, TaxiInformation.GLOSSY_DESCRIPTION),
    ])
    @allure.title("отображение всплывающего окна с описанием тарифа")
    def test_tariff_informaition_displaying(self, driver, tariff, i_button, title, descreption, title_expected, descreption_expected):
        page = TaxiPage(driver)
        page.go_to_taxi_page()
        page.click(tariff)
        page.hover_on_elem(i_button)

        assert page.get_text(descreption) == descreption_expected
        assert page.get_text(title) == title_expected

    @allure.title("под тарифами отображается блок с полями Телефон," \
    "Способ оплаты, Комментарий водителю, Требования к заказу Заказ тарифа Такси")
    def test_order_details_fields_are_displayed(self, driver):
        page = TaxiPage(driver)
        page.go_to_taxi_page()

        assert page.is_displayed(TaxiPageLocators.PHONE_FIELD)
        assert page.is_displayed(TaxiPageLocators.PAYMENT_METHOD_BUTTON)
        assert page.is_displayed(TaxiPageLocators.COMMENT_FIELD)
        assert page.is_displayed(TaxiPageLocators.REQUIREMENTS_BUTTON)

    @allure.title("появляется окно ожидания машины")
    def test_waiting_taxi_page_is_displayed(self, driver):
        page = TaxiPage(driver)
        page.go_to_car_search_page()

        assert page.is_displayed(TaxiPageLocators.TIMER)
        assert page.is_displayed(TaxiPageLocators.CANCEL_BUTTON)
        assert page.is_displayed(TaxiPageLocators.DETAILS_BUTTON)
        assert page.is_displayed(TaxiPageLocators.CAR_SEARCH_TITLE)

    @allure.title("появляется окно ожидания машины")
    def test_completed_order_page_is_displayed(self, driver):
        page = TaxiPage(driver)
        page.go_to_completed_order_page()

        assert page.is_displayed(TaxiPageLocators.CAR_NUMBER)
        assert page.is_displayed(TaxiPageLocators.TARIFF_IMAGE)
        assert page.is_displayed(TaxiPageLocators.DRIVER_NAME)
        assert page.is_displayed(TaxiPageLocators.DRIVER_RAITING)
        assert page.is_displayed(TaxiPageLocators.FIN_CANCEL_BUTTON)
        assert page.is_displayed(TaxiPageLocators.FIN_DETAILS_BUTTON)

    @allure.title("указана стоимость, которая была при выборе тарифа")
    def test_check_cost(self, driver):
        page = TaxiPage(driver)
        page.go_to_taxi_page()
        page.click(TaxiPageLocators.WORK_TARIFF)
        expexted_cost = page.get_cost_number(TaxiPageLocators.EXPECTED_COST)
        page.click(TaxiPageLocators.REQUIREMENTS_BUTTON)
        page.click(TaxiPageLocators.CHECK_BOX)
        page.click(TaxiPageLocators.MAKE_ODER_BUTTON)
        page.wait_element_visability(TaxiPageLocators.COMPLETED_ODER_TITLE)
        page.click(TaxiPageLocators.FIN_DETAILS_BUTTON)

        assert expexted_cost == page.get_cost_number(TaxiPageLocators.FIN_COST)

    @allure.title("отмена заказа")
    def test_cancel_order(self, driver):
        page = TaxiPage(driver)
        page.go_to_completed_order_page()
        page.click(TaxiPageLocators.CANCEL_BUTTON)

        assert page.is_displayed(TaxiPageLocators.MAKE_ODER_BUTTON)