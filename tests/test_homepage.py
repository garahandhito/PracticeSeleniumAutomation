import unittest
from selenium import webdriver
from resources import general_functions


class TestHomepage(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--log-level=3')
        driver = webdriver.Chrome(options=options)
        self.driver = driver
        home = general_functions.GeneralFunctions(self.driver)
        home.open_website()

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        """ Clicking website logo should redirect to homepage """
        home = general_functions.GeneralFunctions(self.driver)
        home.click_on_logo()
        home.homepage_should_open()

if __name__ == '__main__':
    unittest.main()
