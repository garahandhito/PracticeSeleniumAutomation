from resources.common.general_functions import GeneralFunctions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time


class HomepageDict(dict):

	def __getattribute__(self, item):
		if item in self:
			return self[item]
		raise AttributeError

	BANNER_ADS = {1: (By.XPATH, '//img[contains(@src, "themeconfigurator/img/banner-img6.jpg")]'),
				  2: (By.XPATH, '//img[contains(@src, "themeconfigurator/img/banner-img7.jpg")]')}
	HOME_PRODUCT_TABS = {'popular': (By.CSS_SELECTOR, 'a.homefeatured'),
						 'best sellers': (By.CSS_SELECTOR, 'a.blockbestsellers')}


class HomepageLocators(object):

	HOMEPAGE_SLIDER = (By.ID, 'homeslider')
	HOMESLIDER_NEXT = (By.CSS_SELECTOR, 'a.bx-next')
	HOMESLIDER_PREV = (By.CSS_SELECTOR, 'a.bx-prev')
	HOMESLIDER_IMAGES = [(By.XPATH, '//img[contains(@src, "homeslider/images/sample-1.jpg")]'),
						 (By.XPATH, '//img[contains(@src, "homeslider/images/sample-2.jpg")]'),
						 (By.XPATH, '//img[contains(@src, "homeslider/images/sample-3.jpg")]')]
	BANNER_REDIRECTION = (By.CSS_SELECTOR, 'a[href="https://www.prestashop.com/en"]')
	HOVER_ADD_TO_CART = (By.CSS_SELECTOR, 'a.button.ajax_add_to_cart_button')
	CLOSE_CART_WINDOW = (By.CSS_SELECTOR, 'span[title="Close Window"]')


class HomepageController(GeneralFunctions):

	def __init__(self, driver):
		GeneralFunctions.__init__(self, driver)
		self.driver = driver

	def __get_homeslider_state(self):
		homeslider_state = self.driver.find_element(*HomepageLocators.HOMEPAGE_SLIDER).get_attribute('style')
		return homeslider_state

	def scroll_homeslider(self, direction):
		state_1 = self.__get_homeslider_state()
		if direction.lower() == 'next' or direction.lower() == 'right':
			scroll_locator = HomepageLocators.HOMESLIDER_NEXT
		elif direction.lower() == 'prev' or direction.lower() == 'left':
			scroll_locator = HomepageLocators.HOMESLIDER_PREV
		else:
			print('Invalid argument: ' + direction)
			raise UnboundLocalError
		super().select_item(scroll_locator)
		time.sleep(0.5)
		state_2 = self.__get_homeslider_state()
		assert state_1 != state_2, 'Failed to scroll homeslider'

	def __get_homeslider_status(self, locator):
		try:
			WebDriverWait(self.driver, 1).until(ec.visibility_of_element_located(locator))
			return True
		except TimeoutException:
			return False

	def check_homeslider_image(self):
		sample = 0
		while False:
			for image in HomepageLocators.HOMESLIDER_IMAGES:
				self.__get_homeslider_status(image)
				sample += 1
			if sample >= 3:
				print('Image not found')
				raise ValueError
			else:
				print('Image found')
				break

	def check_banner_ads(self, number):
		super().wait_for_checking(HomepageDict.BANNER_ADS[number])
		super().select_item(HomepageDict.BANNER_ADS[number])
		super().wait_for_checking(HomepageLocators.BANNER_REDIRECTION, message='Failed to open redirection')

	def __get_home_products_list(self, tab):
		products = []
		products_container = self.driver.find_element(HomepageDict.HOME_PRODUCT_TABS[tab.lower()])
		products_list = products_container.find_elements(By.CSS_SELECTOR, 'li')
		for product in products_list:
			container = product.find_element(By.CSS_SELECTOR, 'div.product-container')
			left_block = container.find_element(By.CSS_SELECTOR, 'div.left-block')
			image_container = left_block.find_element(By.CSS_SELECTOR, 'div.product-image-container')
			product_name = image_container.find_element(By.CSS_SELECTOR, 'a.product)img_link').get_attribute('title')
			products.append(product_name)
		return products

	def select_home_product_tabs(self, tab):
		before = self.__get_home_products_list(tab).copy()
		try:
			super().select_item(HomepageDict.HOME_PRODUCT_TABS[tab.lower()])
			home_product_tab = self.driver.find_element(HomepageDict.HOME_PRODUCT_TABS[tab.lower()])
			assert 'active' in home_product_tab.find_element_by_xpath('..')
			time.sleep(0.5)
			after = self.__get_home_products_list(tab).copy()
			assert before != after
		except AttributeError:
			print('Home product tab not found')
			raise
		except AssertionError:
			print('Home product tab does not work')
			raise

	def add_to_cart(self, product_name):
		super().hover_on_item((By.XPATH, '//a[contains(@title, "' + product_name + '")]'))
		super().wait_for_button(HomepageLocators.HOVER_ADD_TO_CART)
		super().select_item(HomepageLocators.HOVER_ADD_TO_CART)
		super().wait_for_button(HomepageLocators.CLOSE_CART_WINDOW)
		super().select_item(HomepageLocators.CLOSE_CART_WINDOW)
