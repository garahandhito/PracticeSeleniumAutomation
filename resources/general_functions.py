from resources.utility import Utility
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class GeneralLocators(object):

    LOGO = (By.CSS_SELECTOR, 'img.logo.img-responsive')
    HOMEPAGE_SLIDER = (By.ID, 'homeslider')


class GeneralFunctions(Utility):

    def __init__(self, driver):
        Utility.__init__(self, driver)
        self.driver = driver

    def open_website(self):
        self.driver.get('http://automationpractice.com/')
        super().wait_for_checking(GeneralLocators.LOGO)

    def click_on_logo(self):
        logo = self.driver.find_element(*GeneralLocators.LOGO)
        super().select_item(logo)

    def homepage_should_open(self):
        try:
            super().wait_for_checking(GeneralLocators.LOGO)
            assert 'http://automationpractice.com/index.php' in self.driver.current_url
            # assert str(self.driver.current_url()) == 'http://automationpractice.com/index.php'
            super().wait_for_checking(GeneralLocators.HOMEPAGE_SLIDER)
        except (AssertionError, TimeoutException) as e:
            print('Homepage is not open')
            raise e