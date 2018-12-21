from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class Utility(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_for_checking(self, locator, timeout=2):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def wait_for_button(self, locator, timeout=2):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def wait_for_loading(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def hover_on_item(self, item):
        action = ActionChains(self.driver)
        action.move_to_element(item)
        action.perform()

    def select_item(self, item):
        self.hover_on_item(item)
        item.click()

    def input_item(self, field, item):
        self.select_item(field)
        field.clear()
        field.send_keys(item)

    def select_from_dropdown(self, dropdown, item):
        self.select_item(dropdown)
        time.sleep(0.5)
        selected_item = self.driver.find_element_by_xpath('//li[contains(text(), "' + item + '")]')
        self.select_item(selected_item)

    @staticmethod
    def error_response(argument):
        print('Inappropriate argument: ' + argument)
        raise ValueError
