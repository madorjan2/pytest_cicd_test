import time

import pytest
import allure

from libs.basics.create_driver import get_preconfigured_chrome_driver
from libs.basics.docs_classes import TestCycle, TestCase, TestStep
from libs.basics.allure_utils import priority_zephyr_to_allure
from libs.basics.sql_db import Query

from libs.login_page.pom import LoginPage
from libs.registration_page.pom import RegistrationPage
from libs.registration_page.user import User
from libs.registration_page.utils import fill_out_form

CYCLE_NAME = 'Registration page'
CYCLE_DESCRIPTION = 'Performing functional and non-functional, front-end and end-to-end tests on the moovsmart registration page'
CYCLE_FOLDER = '/FE'
TC_FOLDER = '/FE/registration'

@pytest.fixture(scope='session', autouse=True)
def get_test_cycle():
	test_cycle = TestCycle(name=CYCLE_NAME,
							description=CYCLE_DESCRIPTION,
							folder=CYCLE_FOLDER)
	yield test_cycle
	test_cycle.save_to_json()

class TestRegistrationFunctionality:

	def setup_method(self):
		self.page = RegistrationPage(get_preconfigured_chrome_driver(headless=True))
		self.page.open()
		self.user = User()
		self.query = Query()

	def teardown_method(self):
		self.page.quit()

	def test_registration_with_valid_input(self, get_test_cycle):
		tc = TestCase(name='Registration function - valid input',
						objective='Assert that registration is successful providing valid data',
						precondition='Registration page loads, database is available',
						priority='High',
						folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('positive')

		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.set_expected_result('The submit button is enabled and clickable')

		assert_button = self.page.button_submit().is_enabled()
		ts.set_status('passed' if assert_button else 'failed')
		assert assert_button

		# TODO

		# ts = TestStep(step='Click on the submit button',
		# 				data='',
		# 				expected='The user gets an overlay letting them know the registration was successful.')
		# tc.add_test_step(ts)
		self.page.button_submit().click()
		#
		# assert_redirected = self.page.get_url() != self.page.url
		# ts.set_status('passed' if assert_redirected else 'failed')
		# assert assert_redirected
		time.sleep(10)

		ts = TestStep(step='Check that user is actually created in the database',
						data=self.user.get_query(),
						expected='The query returns exactly one record')
		tc.add_test_step(ts)

		assert_query = len(self.query.get_dict(self.user.get_query())) == 1
		ts.set_status('passed' if assert_query else 'failed')
		assert assert_query

	def test_registration_with_empty_username(self, get_test_cycle):

		expected_error_message = 'Érvénytelen felhasználónév!'

		tc = TestCase(name='Registration function - empty username',
						objective='Assert that user gets correct error message on failing to fill in the username input field',
						precondition='Registration page loads, database is available',
						priority='Normal',
						folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_username('')
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
								  and self.page.error_message_username().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message

	def test_registration_with_empty_password(self, get_test_cycle):

		# TODO once fixed
		expected_error_message = 'Érvénytelen jelszó!'

		tc = TestCase(name='Registration function - empty password',
						objective='Assert that user gets correct error message on failing to fill in the password input field',
						precondition='Registration page loads, database is available',
						priority='Normal',
						folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_password('')
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
								  and self.page.error_message_password().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message

	def test_registration_with_empty_password_confirmation(self, get_test_cycle):

		expected_error_message = 'Jelszavak nem egyeznek!'

		tc = TestCase(name='Registration function - empty password confirmation',
						objective='Assert that user gets correct error message on failing to fill in the password confirmation input field',
						precondition='Registration page loads, database is available',
						priority='Normal',
						folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_password_confirm('')
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
								  and self.page.error_message_password_confirm().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message

	def test_registration_with_empty_email(self, get_test_cycle):

		# TODO once fixed
		expected_error_message = 'Érvénytelen email cím!'

		tc = TestCase(name='Registration function - empty email',
						objective='Assert that user gets correct error message on failing to fill in the email input field',
						precondition='Registration page loads, database is available',
						priority='Normal',
						folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_email('')
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
								  and self.page.error_message_email().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message

	def test_registration_with_empty_first_name(self, get_test_cycle):

		expected_error_message = 'Érvénytelen keresztnév!'

		tc = TestCase(name='Registration function - empty first name',
						objective='Assert that user gets correct error message on failing to fill in the first name input field',
						precondition='Registration page loads, database is available',
						priority='Normal',
						folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_first_name('')
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
								  and self.page.error_message_first_name().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message

	def test_registration_with_empty_last_name(self, get_test_cycle):

		expected_error_message = 'Érvénytelen vezetéknév!'

		tc = TestCase(name='Registration function - empty first name',
					  objective='Assert that user gets correct error message on failing to fill in the last name input field',
					  precondition='Registration page loads, database is available',
					  priority='Normal',
					  folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_last_name('')
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
										  and self.page.error_message_last_name().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message

	def test_registration_with_empty_phone_number(self, get_test_cycle):

		# TODO on fix
		expected_error_message = 'Érvénytelen vezetéknév!'

		tc = TestCase(name='Registration function - empty first name',
					  objective='Assert that user gets correct error message on failing to fill in the phone number input field',
					  precondition='Registration page loads, database is available',
					  priority='Normal',
					  folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_phone_number('')
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
										  and self.page.error_message_phone_number().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message

	def test_registration_with_too_short_username(self, get_test_cycle):

		expected_error_message = 'Érvénytelen felhasználónév!\nMinimum 6 karaktert kell megadni'

		tc = TestCase(name='Registration function - too short username',
						objective='Assert that user gets correct error message on providing too short username',
						precondition='Registration page loads, database is available',
						priority='Normal',
						folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_username(self.user.get_username()[:3])
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
								  and self.page.error_message_username().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message

	def test_registration_with_too_long_username(self, get_test_cycle):

		expected_error_message = 'Érvénytelen felhasználónév!\nMaximum 15 karakterből állhat'

		tc = TestCase(name='Registration function - too long username',
						objective='Assert that user gets correct error message on providing too long username',
						precondition='Registration page loads, database is available',
						priority='Normal',
						folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_username(self.user.get_username()*4)
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
								  and self.page.error_message_username().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message

	def test_registration_with_accents_in_username(self, get_test_cycle):
		expected_error_message = 'Érvénytelen felhasználónév!\nMaximum 15 karakterből állhat'

		tc = TestCase(name='Registration function - accents in username',
					  objective='Assert that user gets correct error message on providing a username with accents',
					  precondition='Registration page loads, database is available',
					  priority='Normal',
					  folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_username('Áéíöőúüű')
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
										   and self.page.error_message_username().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message

	def test_registration_with_whitespace_in_username(self, get_test_cycle):
		expected_error_message = 'Érvénytelen felhasználónév!\nÉrvénytelen karakter! Elfogadott karakterek: a-z,A-Z,0-9, _\nSzóközt nem tartalmazhat a jelszó!'

		tc = TestCase(name='Registration function - whitespace in username',
					  objective='Assert that user gets correct error message on providing a username with whitespace',
					  precondition='Registration page loads, database is available',
					  priority='Normal',
					  folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_username('john doe')
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
										   and self.page.error_message_username().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message

	def test_registration_with_too_short_password(self, get_test_cycle):

		expected_error_message = 'Érvénytelen jelszó!\nMinimum 8 karakter hosszúnak kell lennie!'

		tc = TestCase(name='Registration function - too short password',
						objective='Assert that user gets correct error message providing a too short password',
						precondition='Registration page loads, database is available',
						priority='Normal',
						folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_password('Aa1')
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
								  and self.page.error_message_password().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message

	def test_registration_with_too_long_password(self, get_test_cycle):

		expected_error_message = 'Érvénytelen jelszó!\nMaximum 20 karakter hosszú lehet!'

		tc = TestCase(name='Registration function - too long password',
						objective='Assert that user gets correct error message providing a too long password',
						precondition='Registration page loads, database is available',
						priority='Normal',
						folder=TC_FOLDER)
		get_test_cycle.add_test_case(tc)
		allure.dynamic.title(tc.name)
		allure.dynamic.description(tc.objective)
		allure.dynamic.severity(priority_zephyr_to_allure(tc.priority))
		allure.dynamic.label('suite', get_test_cycle.name)
		allure.dynamic.tag('frontend')
		allure.dynamic.tag('registration')
		allure.dynamic.tag('negative')

		self.user.set_password('Aa1'*7)
		ts = fill_out_form(self.page, self.user)

		tc.add_test_step(ts)
		ts.append_to_test_data(f'Expected error message: {expected_error_message}')
		ts.set_expected_result('The submit button is disabled and the correct error message is shown')

		assert_button_and_error_message = (not self.page.button_submit().is_enabled()
								  and self.page.error_message_password().text == expected_error_message)
		ts.set_status('passed' if assert_button_and_error_message else 'failed')
		assert assert_button_and_error_message