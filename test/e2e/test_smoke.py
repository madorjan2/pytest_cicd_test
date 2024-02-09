import pytest
import allure

from libs.basics.create_driver import get_preconfigured_chrome_driver
from libs.basics.docs_classes import TestCycle, TestCase, TestStep
from libs.basics.sql_db import Query
from libs.basics.allure_utils import priority_zephyr_to_allure

from libs.login_page.pom import LoginPage
from libs.registration_page.pom import RegistrationPage

CYCLE_NAME = 'Smoke test'
CYCLE_DESCRIPTION = 'Performing smoke test on moovsmart webpage and database'
CYCLE_FOLDER = '/FE'
TC_FOLDER = '/FE/smoke'

@pytest.fixture(scope='session', autouse=True)
def get_test_cycle():
	test_cycle = TestCycle(name=CYCLE_NAME,
							description=CYCLE_DESCRIPTION,
							folder=CYCLE_FOLDER)
	yield test_cycle
	test_cycle.save_to_json()

class TestSmoke:

	def setup_method(self):
		self.page = None

	def teardown_method(self):
		if self.page is not None:
			self.page.quit()

	# TODO
	# def test_mainpage_loads(self):
	# 	assert True

	def test_login_page_loads(self, get_test_cycle):
		tc = TestCase(name='Login page loads succesfully',
										objective='Assert that the login page loads in',
										precondition='',
										priority='High',
										folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('smoke')
		allure.dynamic.tag('login')
		allure.dynamic.tag('positive')


		self.page = LoginPage(get_preconfigured_chrome_driver(headless=True))
		allure.dynamic.link(self.page.url)
		self.page.open()

		ts = TestStep(step='Type the URL into the browser',
						data=self.page.url,
						expected='The page with the given url loads')
		tc.add_test_step(ts)

		assert_url = self.page.get_url() == self.page.url
		ts.set_status('passed' if assert_url else 'failed')
		assert assert_url

	def test_registration_page_loads(self, get_test_cycle):
		tc = TestCase(name='Registration page loads succesfully',
										objective='Assert that the registration page loads in',
										precondition='',
										priority='High',
										folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('smoke')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('positive')

		self.page = RegistrationPage(get_preconfigured_chrome_driver(headless=True))
		allure.dynamic.link(self.page.url)
		self.page.open()

		ts = TestStep(step='Type the URL into the browser',
						data=self.page.url,
						expected='The page with the given url loads')
		tc.add_test_step(ts)

		assert_url = self.page.get_url() == self.page.url
		ts.set_status('passed' if assert_url else 'failed')
		assert assert_url

	def test_sql_connection(self, get_test_cycle):
		tc = TestCase(name='Connecting to database',
										objective='Assert that the database can be connected to',
										precondition='',
										priority='High',
										folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('backend')
		allure.dynamic.tag('smoke')
		allure.dynamic.tag('database')
		allure.dynamic.tag('positive')

		query = 'SELECT * FROM moovsmart.advertisement'
		self.query = Query()

		ts = TestStep(step='Connect to the database and run a simple query',
						data=query,
						expected='The connection is made and the query returns with records')
		tc.add_test_step(ts)

		try:
			results = self.query.get_dict(query)
			assert_valid_query = len(results) > 0
			ts.set_status('passed' if assert_valid_query else 'failed')
			assert assert_valid_query
		except:
			ts.set_status('failed')
			assert False
