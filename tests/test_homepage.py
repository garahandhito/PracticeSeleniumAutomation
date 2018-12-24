import unittest
from selenium import webdriver
from resources import homepage


class TestHomepage(unittest.TestCase):

	def setUp(self):
		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		# options.add_argument('--start-maximized')
		options.add_argument('--log-level=3')
		driver = webdriver.Chrome(options=options)
		self.driver = driver
		home = homepage.HomepageController(self.driver)
		home.open_membersite()

	def tearDown(self):
		self.driver.quit()

	def test_01(self):
		""" Check all 3 homeslider images """
		home = homepage.HomepageController(self.driver)
		home.check_homeslider_image()
		home.scroll_homeslider('next')
		home.check_homeslider_image()
		home.scroll_homeslider('next')
		home.check_homeslider_image()

if __name__ == '__main__':
	unittest.main()
