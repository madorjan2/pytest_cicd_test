import pytest
import allure

from libs.basics.create_driver import get_preconfigured_chrome_driver
from libs.basics.docs_classes import TestCycle, TestCase, TestStep
from libs.basics.allure_utils import priority_zephyr_to_allure

from libs.login_page.pom import LoginPage
from libs.registration_page.pom import RegistrationPage

from selenium.webdriver.remote.webelement import WebElement

CYCLE_NAME = 'Sanity test'
CYCLE_DESCRIPTION = 'Performing sanity test on moovsmart webpages and database'
CYCLE_FOLDER = '/FE'
TC_FOLDER = '/FE/smoke'

@pytest.fixture(scope='session', autouse=True)
def get_test_cycle():
	test_cycle = TestCycle(name=CYCLE_NAME,
							description=CYCLE_DESCRIPTION,
							folder=CYCLE_FOLDER)
	yield test_cycle
	test_cycle.save_to_json()

class TestSanity:

	def setup_method(self):
		self.page = None

	def teardown_method(self):
		if self.page is not None:
			self.page.quit()

	# TODO
	# def test_mainpage(self, get_test_cycle):
	# 	assert True

	def check_visibility_of_element(self, tc: TestCase, name, element: WebElement):
		ts = TestStep(step=f'Check that the {name} is visible',
					  data="",
					  expected=f'The {name} is visible')
		tc.add_test_step(ts)

		assert_visibility = element.is_displayed()
		ts.set_status('passed' if assert_visibility else 'failed')
		assert assert_visibility

	def test_login_page_element_visibility(self, get_test_cycle):
		tc = TestCase(name='Login page - visibility of webelements',
						objective='Assert that all neccessary webelements are visible and interactable on the login page',
						precondition='Login page loads',
						priority='High',
						folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('sanity')
		allure.dynamic.tag('login')
		allure.dynamic.tag('positive')

		self.page = LoginPage(get_preconfigured_chrome_driver(headless=True))
		self.page.open()

		self.check_visibility_of_element(tc, 'navbar home button', self.page.button_home_navbar())

		ts = TestStep(step='Check that the navbar navigation buttons are visible',
					  data="",
					  expected='The navbar navigation buttons are visible')
		tc.add_test_step(ts)

		assert_visibility = self.page.button_ad_list_navbar().is_displayed() and self.page.button_loan_calc_navbar().is_displayed()  and self.page.button_ad_search_navbar().is_displayed()
		ts.set_status('passed' if assert_visibility else 'failed')
		assert assert_visibility

		self.check_visibility_of_element(tc, 'navbar login button', self.page.button_login_navbar())
		self.check_visibility_of_element(tc, 'username input field', self.page.input_username())
		self.check_visibility_of_element(tc, 'password input field', self.page.input_password())
		self.check_visibility_of_element(tc, 'Remember me checkbox', self.page.checkbox_remember())
		self.check_visibility_of_element(tc, 'login button', self.page.button_login())
		self.check_visibility_of_element(tc, 'register button', self.page.button_register())

	def test_registration_page_element_visibility(self, get_test_cycle):
		tc = TestCase(name='Registration page - visibility of webelements',
						objective='Assert that all neccessary webelements are visible and interactable on the registration page',
						precondition='Registration page loads',
						priority='High',
						folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('sanity')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('positive')

		self.page = RegistrationPage(get_preconfigured_chrome_driver(headless=True))
		self.page.open()

		self.check_visibility_of_element(tc, 'navbar home button', self.page.button_home_navbar())

		ts = TestStep(step='Check that the navbar navigation buttons are visible',
					  data="",
					  expected='The navbar navigation buttons are visible')
		tc.add_test_step(ts)

		assert_visibility = self.page.button_ad_list_navbar().is_displayed() and self.page.button_loan_calc_navbar().is_displayed() and self.page.button_ad_search_navbar().is_displayed()
		ts.set_status('passed' if assert_visibility else 'failed')
		assert assert_visibility

		self.check_visibility_of_element(tc, 'navbar login button', self.page.button_login_navbar())
		self.check_visibility_of_element(tc, 'username input field', self.page.input_username())
		self.check_visibility_of_element(tc, 'email input field', self.page.input_email())
		self.check_visibility_of_element(tc, 'password input field', self.page.input_password())
		self.check_visibility_of_element(tc, 'password confirmation input field', self.page.input_confirm_password())
		self.check_visibility_of_element(tc, 'first name input field', self.page.input_first_name())
		self.check_visibility_of_element(tc, 'last name input field', self.page.input_last_name())
		self.check_visibility_of_element(tc, 'phone number input field', self.page.input_phone_number())
		self.check_visibility_of_element(tc, 'terms and conditions checkbox', self.page.checkbox_terms())
		self.check_visibility_of_element(tc, 'terms and conditions link', self.page.button_terms())
		self.check_visibility_of_element(tc, 'submit button', self.page.button_submit())

	def test_refresh(self, get_test_cycle):
		tc = TestCase(name='Refresh webpage',
					  objective='Assert that refreshing the webpage works',
					  precondition='Registration page loads, webelements are visible',
					  priority='High',
					  folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('sanity')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('positive')

		self.page = RegistrationPage(get_preconfigured_chrome_driver(headless=True))
		self.page.open()

		dummy_text = 'test'
		ts = TestStep(step='Fill in the username input field',
					  data=dummy_text,
					  expected='The text shows up in the input field')
		tc.add_test_step(ts)

		self.page.input_username().send_keys(dummy_text)
		assert_text_is_displayed = self.page.input_username().get_attribute('value') == dummy_text
		ts.set_status('passed' if assert_text_is_displayed else 'failed')
		assert assert_text_is_displayed

		ts = TestStep(step='Refresh the website',
					  data='',
					  expected='The username input field holds no text')
		tc.add_test_step(ts)

		self.page.refresh()
		assert_text_is_displayed = self.page.input_username().get_attribute('value') == ''
		ts.set_status('passed' if assert_text_is_displayed else 'failed')
		assert assert_text_is_displayed

	def test_backward_and_forward_navigation(self, get_test_cycle):
		tc = TestCase(name='Navigation backwards and forward',
					  objective='Assert that navigating backwards and forward is working properly',
					  precondition='Registration page loads, Login page loads, Login page elements are visible',
					  priority='High',
					  folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('sanity')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('login')
		allure.dynamic.tag('positive')

		self.page = LoginPage(get_preconfigured_chrome_driver(headless=True))

		ts = TestStep(step='Open the login page',
					  data=self.page.get_url(),
					  expected='The login page loads')
		tc.add_test_step(ts)
		self.page.open()

		assert_loaded = self.page.get_url() == self.page.url
		ts.set_status('passed' if assert_loaded else 'failed')
		assert assert_loaded

		ts = TestStep(step='Click on the registration button',
					  data='',
					  expected='The registration page loads')
		tc.add_test_step(ts)

		self.page.button_register().click()
		self.page = RegistrationPage(self.page.driver)

		assert_loaded = self.page.get_url() == self.page.url
		ts.set_status('passed' if assert_loaded else 'failed')
		assert assert_loaded

		ts = TestStep(step='Click on the back button in the browser',
					  data='',
					  expected='The login page loads')
		tc.add_test_step(ts)

		self.page.back()
		self.page = LoginPage(self.page.driver)

		assert_loaded = self.page.get_url() == self.page.url
		ts.set_status('passed' if assert_loaded else 'failed')
		assert assert_loaded

		ts = TestStep(step='Click on the forward button in the browser',
					  data='',
					  expected='The registration page loads')
		tc.add_test_step(ts)

		self.page.forward()
		self.page = RegistrationPage(self.page.driver)

		assert_loaded = self.page.get_url() == self.page.url
		ts.set_status('passed' if assert_loaded else 'failed')
		assert assert_loaded