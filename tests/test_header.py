import unittest
from selenium import webdriver
from resources import homepage


class TestHeader(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--start-maximized')
        options.add_argument('--log-level=3')
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        self.driver = driver
        head = homepage.HomepageController(self.driver)
        head.open_membersite()
        head.homepage_should_open()

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        """ Click website logo should open homepage """
        head = homepage.HomepageController(self.driver)
        head.click_on_logo()
        head.homepage_should_open()

    def test_02(self):
        """ Click Contact Us link should open Contact Us page """
        head = homepage.HomepageController(self.driver)
        head.open_contact_us()

    def test_03(self):
        """ Click Sign In link should open Sign In page """
        head = homepage.HomepageController(self.driver)
        head.open_sign_in_page()

    def test_04(self):
        """ Click Sign Out should sign the user out """
        head = homepage.HomepageController(self.driver)
        head.open_sign_in_page()
        head.sign_in_as('kamnyet@kamnyet.com', 'biji123')
        head.sign_out()

    def test_05(self):
        """ Item found when existing item name is inputted as keyword """
        head = homepage.HomepageController(self.driver)
        head.search_item('Short Sleeve')
        head.search_item_is_found()

    @unittest.expectedFailure
    def test_06(self):
        """ Item is not found when non-existing item name is inputted as keyword """
        head = homepage.HomepageController(self.driver)
        head.search_item('Blademail')
        head.search_item_is_found()

    @unittest.expectedFailure
    def test_07(self):
        """ Item found if numbers and symbols are inputted, if such item name exist """
        head = homepage.HomepageController(self.driver)
        head.search_item('123!@#')
        head.search_item_is_found()

    def test_08(self):
        """ Click account name should open My Account page """
        head = homepage.HomepageController(self.driver)
        head.open_sign_in_page()
        head.sign_in_as('kamnyet@kamnyet.com', 'biji123')
        head.open_account()


if __name__ == '__main__':
    unittest.main()
