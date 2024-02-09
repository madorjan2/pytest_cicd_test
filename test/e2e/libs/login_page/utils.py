from test.e2e.libs.login_page.pom import LoginPage
from test.e2e.libs.login_page.login_user import RegisteredUser
from test.e2e.libs.basics.docs_classes import TestStep


def fill(page: LoginPage, user: RegisteredUser):
	page.input_username().send_keys(user.get_username())
	page.input_password().send_keys(user.get_password())
	page.button_login().click()
	return TestStep(step='Kitoltjuk az email es password mezoket, majd megnyomjuk a Belepes gombot',
					data=str(user))


def toggle_remember(page: LoginPage):
	page.checkbox_remember().click()
	return TestStep(step='Raklikkelunk az emlekezz ram gombra',
					data="")


def toggle_password_visibility(page: LoginPage):
	page.button_view_password().click()
	return TestStep(step='Raklikkelunk a jelszo megjelenito gombra',
					data="")


def click_on_registration_button(page: LoginPage):
	page.button_register().click()
	return TestStep(step='Rakattintunk a fiok letrehozasa gombra',
					data="")
