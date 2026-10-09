import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
#pytest tests/test_route_drawing.py

class TestRouteDrawing:
    @allure.title("на карте отображаются две точки начала и конца маршрута")
    def test_route_points_are_displayed(self, driver):
        page = MainPage(driver)
        page.build_route()

        assert page.is_displayed(MainPageLocators.MARK_A)
        assert page.is_displayed(MainPageLocators.MARK_B)
