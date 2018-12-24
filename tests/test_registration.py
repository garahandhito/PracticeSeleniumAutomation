import unittest
from selenium import webdriver
from resources.common import general_functions


class TestRegistration(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--start-maximized')
        options.add_argument('--log-level=3')
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        self.driver = driver
        reg = general_functions.GeneralFunctions(self.driver)
        reg.open_membersite()
        reg.homepage_should_open()

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        """ This test case is to reproduce registration issue about using double dot
         in the middle of local part should be unaccepted """
        reg = general_functions.GeneralFunctions(self.driver)
        reg.open_sign_in_page()
        reg.create_account_email('double..dot@email.com')
        reg.email_should_unaccepted()

    def test_02(self):
        """ This test case is to reproduce registration issue about using double dot
         in the middle of local part should be accepted """
        reg = general_functions.GeneralFunctions(self.driver)
        reg.open_sign_in_page()
        reg.create_account_email('"double..dot"@email.com')
        reg.email_should_accepted()


if __name__ == '__main__':
    unittest.main()
