import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
import re

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод, чтобы кликнуть на элемент')
    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Метод, чтобы получить текст элемента')
    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).text

    @allure.step('проверка видимости элемента')
    def is_displayed(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).is_displayed()
    
    @allure.step('заполнение поля')
    def send_keys(self, locator, value):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(value) 
    
    @allure.step('ожидание появления элемента')
    def wait_element_visability(self, locator):
        self.driver.implicitly_wait(40)
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
    
    @allure.step('элемент кликабелен')
    def element_is_clickable(self, locator):
        return  WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
    
    @allure.step('наведение курсора на элемент')
    def hover_on_elem(self, locator):
        try:
            element = self.find_element(locator) 
            is_visible = element.is_displayed()
            if is_visible:
                self.driver.implicitly_wait(10)
                element  = self.driver.find_element(*locator)
                action = ActionChains(self.driver).move_to_element(element)
                action.perform()
            return is_visible
        except NoSuchElementException:
            return False
        
    def find_element(self, locator):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def get_the_price(self, locator):
        element = self.find_element(locator)
        text = element.text.strip()
        return text
    
    def get_cost_number(self, locator) -> int:
        text = self.get_text(locator)
        match = re.search(r"\d+", text)
        return int(match.group()) if match else 0