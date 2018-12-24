from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class Utility(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_for_checking(self, locator, timeout=2, message=''):
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            print(message)
            raise

    def wait_for_button(self, locator, timeout=2, message=''):
        try:
            WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
        except TimeoutException:
            print(message)
            raise

    def wait_for_loading(self, locator, timeout=2, message=''):
        try:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))
        except TimeoutException:
            print(message)
            raise

    def hover_on_item(self, locator):
        item = self.driver.find_element(*locator)
        action = ActionChains(self.driver)
        action.move_to_element(item)
        action.perform()

    def select_item(self, locator):
        self.hover_on_item(locator)
        self.driver.find_element(*locator).click()

    def type_to_field(self, field_locator, item):
        field = self.driver.find_element(*field_locator)
        self.select_item(field_locator)
        field.clear()
        field.send_keys(item)

    def select_from_dropdown(self, dropdown_locator, item_locator):
        self.select_item(dropdown_locator)
        self.wait_for_loading(item_locator)
        self.select_item(item_locator)

    @staticmethod
    def error_response(argument):
        print('Inappropriate argument:' + str(argument))
        raise ValueError
