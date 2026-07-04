import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
#pytest tests/test_taxi_fare_ordering.py

class TestTaxiFareOrdering:
    @allure.title("под выбором адресов отображается блок с выбором маршрута")
    def test_taxi_fare_select_is_displayed(self, driver):
        page = MainPage(driver)
        page.build_route()

        assert page.is_displayed(MainPageLocators.TYPE_PICKER_BLOCK)

    @allure.title('ввод одинакового адреса в поля "Откуда" и "Куда"' )
    def test_route_with_2_same_addresses(self, driver):
        page = MainPage(driver)
        page.build_route_same_adress()

        assert page.is_displayed(MainPageLocators.TYPE_PICKER_BLOCK)
        assert page.is_displayed(MainPageLocators.MARKS_A_AND_B_SAME_OUTPUT)