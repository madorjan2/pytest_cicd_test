import random
from faker import Faker

from libs.basics.sql_db import Query

# fake = Faker(locale='hu_HU')
fake = Faker()


def get_fake_phone_number():
	fake_phone_number = random.randint(1000000, 9999999)
	return '+36' + random.choice(['20', '30', '70']) + str(fake_phone_number)


class User:
	def __init__(self, username=None, email=None, password=None, password_confirm=None, phone_number=None,
				 first_name=None,
				 last_name=None, terms=None):
		self.username = username
		self.email = email
		self.password = password
		self.password_confirm = password_confirm
		self.phone_number = phone_number
		self.first_name = first_name
		self.last_name = last_name
		self.terms = terms

		if self.email is None:
			self.email = fake.ascii_safe_email()
		if self.username is None:
			self.username = self.email.split("@")[0]
			while len(self.username) < 6:
				self.username = self.username * 2
		if self.password is None:
			self.password = fake.password(length=8, special_chars=False, digits=True, upper_case=True, lower_case=True)
		if self.password_confirm is None:
			self.password_confirm = self.password
		if self.phone_number is None:
			self.phone_number = get_fake_phone_number()
		if self.first_name is None:
			self.first_name = fake.first_name()
		if self.last_name is None:
			self.last_name = fake.last_name()
		if self.terms is None:
			self.terms = True

		self.orig_username = self.username
		self.orig_email = self.email
		self.orig_password = self.password
		self.orig_password_confirm = self.password_confirm
		self.orig_phone_number = self.phone_number
		self.orig_first_name = self.first_name
		self.orig_last_name = self.last_name
		self.orig_terms = self.terms

	def __str__(self):
		return (f'Username: {self.username}\n'
				f'Email: {self.email}\n'
				f'Password: {self.password}\n'
				f'Password confirm: {self.password_confirm}\n'
				f'Phone number: {self.phone_number}\n'
				f'First name: {self.first_name}\n'
				f'Last name: {self.last_name}\n'
				f'Terms: {self.terms}')

	def get_email(self):
		return self.email

	def set_email(self, email):
		self.email = email

	def get_password(self):
		return self.password

	def set_password(self, password):
		self.password = password

	def get_password_confirm(self):
		return self.password_confirm

	def set_password_confirm(self, password_confirm):
		self.password_confirm = password_confirm

	def get_username(self):
		return self.username

	def set_username(self, username):
		self.username = username

	def get_phone_number(self):
		return self.phone_number

	def set_phone_number(self, phone_number):
		self.phone_number = phone_number

	def get_last_name(self):
		return self.last_name

	def set_last_name(self, last_name):
		self.last_name = last_name

	def get_first_name(self):
		return self.first_name

	def set_first_name(self, first_name):
		self.first_name = first_name

	def get_terms(self):
		return self.terms

	def set_terms(self, terms):
		self.terms = terms

	def restore(self):
		self.email = self.orig_email
		self.password = self.orig_password
		self.password_confirm = self.orig_password_confirm
		self.username = self.orig_username
		self.phone_number = self.orig_phone_number
		self.first_name = self.orig_first_name
		self.last_name = self.orig_last_name
		self.terms = self.orig_terms

	def get_query(self):
		return (f'SELECT *\n'
				f'FROM app_user\n'
				f'WHERE email = "{self.email}"\n'
				f'AND first_name = "{self.first_name}"\n'
				f'AND last_name = "{self.last_name}"\n'
				f'AND username = "{self.username}"\n'
				f'AND phone_number = "{self.phone_number}";')

	def get_confirmation_token(self):
		result_dict = Query().get_dict(f'SELECT token\n'
									   f'FROM verification_token\n'
									   f'INNER JOIN moovsmart.app_user\n'
									   f'ON verification_token.app_user_id = app_user.id\n'
									   f'WHERE email = "{self.email}"\n'
									   f'AND first_name = "{self.first_name}"\n'
									   f'AND last_name = "{self.last_name}"\n'
									   f'AND username = "{self.username}"\n'
									   f'AND phone_number = "{self.phone_number}";')
		return result_dict[0]['token']

	def verify_through_database(self):
		result_dict = Query().get_dict(self.get_query())
		id = result_dict[0]['id']
		Query().update_db(f'UPDATE app_user\nSET active = 1\nWHERE id = {id};')
