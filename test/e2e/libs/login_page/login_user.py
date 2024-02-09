class RegisteredUser:
	def __init__(self, username='madorjan', password='Asdf1234'):
		self.username = username
		self.password = password

		self.username_orig = username
		self.password_orig = password

	def __str__(self):
		return f'Username: {self.username}\nPassword: {self.password}'

	def get_username(self):
		return self.username

	def get_password(self):
		return self.password

	def del_username(self):
		self.username = ''

	def del_password(self):
		self.password = ''

	def restore(self):
		self.username = self.username_orig
		self.password = self.password_orig

	def get_query(self):
		return f'SELECT * FROM hotel.account WHERE email = "{self.email}"'
