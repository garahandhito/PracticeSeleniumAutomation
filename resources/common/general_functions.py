from resources.common.utility import Utility
from selenium.webdriver.common.by import By
import time


class GeneralDict(dict):

	def __getattribute__(self, item):
		if item in self:
			return self[item]
		raise AttributeError(item)

	TABS = {'women': (By.CSS_SELECTOR, 'a[title="Women"]'),
			'dresses': (By.CSS_SELECTOR, 'a[title="Dresses"]'),
			't-shirts': (By.CSS_SELECTOR, 'a[title="T-shirts"]')}
	WOMEN = {'tops': (By.CSS_SELECTOR, 'a[title="Tops"]'),
			 'dresses': (By.CSS_SELECTOR, 'a[title="Dresses"]')}
	WOMEN_TOPS = {'t-shirts': (By.CSS_SELECTOR, 'a[title="T-shirts"]'),
				  'blouses': (By.CSS_SELECTOR, 'a[title="Blouses"]')}
	WOMEN_DRESSES = {'casual dresses': (By.CSS_SELECTOR, 'a[title="Casual Dresses"]'),
					 'evening dresses': (By.CSS_SELECTOR, 'a[title="Evening Dresses"]'),
					 'summer dresses': (By.CSS_SELECTOR, 'a[title="Summer Dresses"]')}


class GeneralLocators(object):

	LOGO = (By.CSS_SELECTOR, 'img.logo.img-responsive')
	HOMEPAGE_SLIDER = (By.ID, 'homeslider')
	CONTACT_US_LINK = (By.ID, 'contact-link')
	CONTACT_US_FORM = (By.CSS_SELECTOR, 'form.contact-form-box')
	SIGN_IN_LINK = (By.CSS_SELECTOR, 'a.login')
	SIGN_OUT_LINK = (By.CSS_SELECTOR, 'a.logout')
	EMAIL_FIELD = (By.ID, 'email')
	PASSWORD_FIELD = (By.ID, 'passwd')
	CREATE_EMAIL_FIELD = (By.ID, 'email_create')
	SUBMIT_LOGIN = (By.ID, 'SubmitLogin')
	ACCOUNT_NAME = (By.CSS_SELECTOR, 'a.account')
	ACCOUNT_MENU = (By.CSS_SELECTOR, 'ul.myaccount-link-list')
	SEARCHBAR_FIELD = (By.ID, 'search_query_top')
	SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.button-search')
	SEARCH_RESULT_COUNTER = (By.CSS_SELECTOR, 'span.heading-counter')
	CART_QTY = (By.CSS_SELECTOR, 'span.ajax_cart_quantity')
	CART_EMPTY = (By.CSS_SELECTOR, 'span.ajax_cart_no_product')
	TABS = [(By.CSS_SELECTOR, 'a[title="Women"]'),
			(By.CSS_SELECTOR, 'a[title="Dresses"]'),
			(By.CSS_SELECTOR, 'a[title="T-shirts"]')]
	EMAIL_CREATE_ERROR = (By.ID, 'create_account_error')
	SUBMIT_CREATE = (By.ID, 'SubmitCreate')
	CREATE_ACCOUNT_FORM = (By.ID, 'account-creation_form')


class GeneralFunctions(Utility):

	def __init__(self, driver):
		Utility.__init__(self, driver)
		self.driver = driver

	def open_membersite(self):
		self.driver.get('http://automationpractice.com')

	def homepage_should_open(self):
		super().wait_for_checking(GeneralLocators.LOGO, message='Failed to open membersite')
		super().wait_for_checking(GeneralLocators.HOMEPAGE_SLIDER)
		assert 'http://automationpractice.com/index.php' in self.driver.current_url, 'Failed to open homepage'

	def click_on_logo(self):
		super().select_item(GeneralLocators.LOGO)

	def open_contact_us(self):
		super().select_item(GeneralLocators.CONTACT_US_LINK)
		super().wait_for_checking(GeneralLocators.CONTACT_US_FORM, message='Failed to open Contact Us page')

	def open_sign_in_page(self):
		super().select_item(GeneralLocators.SIGN_IN_LINK)
		super().wait_for_checking(GeneralLocators.EMAIL_FIELD, message='Failed to open Sign In page')

	def sign_in_as(self, email, password):
		super().type_to_field(GeneralLocators.EMAIL_FIELD, email)
		super().type_to_field(GeneralLocators.PASSWORD_FIELD, password)
		super().select_item(GeneralLocators.SUBMIT_LOGIN)
		super().wait_for_checking(GeneralLocators.SIGN_OUT_LINK, message='Failed to sign in')

	def open_account(self):
		super().select_item(GeneralLocators.ACCOUNT_NAME)
		super().wait_for_checking(GeneralLocators.ACCOUNT_MENU)

	def sign_out(self):
		super().select_item(GeneralLocators.SIGN_OUT_LINK)
		super().wait_for_checking(GeneralLocators.SIGN_IN_LINK, message='Failed to sign out')

	def search_item(self, item):
		super().type_to_field(GeneralLocators.SEARCHBAR_FIELD, item)
		time.sleep(0.25)
		super().select_item(GeneralLocators.SEARCH_BUTTON)

	def search_item_is_found(self):
		super().wait_for_checking(GeneralLocators.SEARCH_RESULT_COUNTER, message='Failed to search item')

	def verify_cart_quantity(self, qty):
		if qty > 0:
			assert str(qty) in self.driver.find_element(*GeneralLocators.CART_QTY).get_attribute('innerHTML')
			assert 'display: inline;' in self.driver.find_element(*GeneralLocators.CART_QTY).get_attribute('style')
		else:
			assert 'display: inline;' in self.driver.find_element(*GeneralLocators.CART_EMPTY).get_attribute('style')

	def open_tab(self, tab):
		super().select_item(GeneralDict.TABS[tab.lower()])

	# skip dulu, susah, selectornya dobel2 :(
	# def select_category_from_tab(self, tab, category, subcat=''):
	# 	super().hover_on_item(GeneralDict.TABS[tab.lower()])
	# 	if subcat == '':
	# 		if tab.lower() == 'women':
	# 			super().select_item(GeneralDict.WOMEN[category.lower()])
	# 		elif tab.lower() == 'dresses':
	# 			super().select_item(GeneralDict.WOMEN_DRESSES[category.lower()])
	# 	else:
	# 		if tab.lower() == 'women':
	# 			if category.lower() == 'tops':
	# 				super().select_item(GeneralDict.WOMEN_TOPS[subcat.lower()])
	# 			elif category.lower() == 'dresses':
	# 				super().select_item(GeneralDict.WOMEN_DRESSES.)
	# 		else:
	# 			print('No subcategory found')

	def email_should_unaccepted(self):
		super().wait_for_checking(GeneralLocators.EMAIL_CREATE_ERROR, message='Email should be unaccepted')

	def email_should_accepted(self):
		super().wait_for_checking(GeneralLocators.CREATE_ACCOUNT_FORM, timeout=5, message='Failed to create account email')

	def create_account_email(self, email):
		super().type_to_field(GeneralLocators.CREATE_EMAIL_FIELD, email)
		super().select_item(GeneralLocators.SUBMIT_CREATE)
