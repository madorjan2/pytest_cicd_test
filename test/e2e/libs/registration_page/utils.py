from libs.registration_page.pom import RegistrationPage
from libs.registration_page.user import User
from ..basics.docs_classes import TestStep

def fill_out_form(page: RegistrationPage, user: User) -> TestStep:
	page.input_username().send_keys(user.get_username())
	page.input_last_name().send_keys(user.get_last_name())
	page.input_first_name().send_keys(user.get_first_name())
	page.input_email().send_keys(user.get_email())
	page.input_phone_number().send_keys(user.get_phone_number())
	page.input_password().send_keys(user.get_password())
	page.input_confirm_password().send_keys(user.get_password_confirm())
	if user.get_terms():
		page.checkbox_terms().click()
	return TestStep(step='Fill out the data form with the following values',
					data=str(user))