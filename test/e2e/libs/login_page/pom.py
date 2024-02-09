from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ..basics.general_model import GeneralPage

DEFAULT_TIMEOUT = 10

class LoginPage(GeneralPage):

	def __init__(self, driver: webdriver.Chrome):
		self.url = 'http://ec2-13-60-30-176.eu-north-1.compute.amazonaws.com/#/login'
		super().__init__(driver, self.url)

	def input_username(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
			EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="loginUsername"]')))

	def input_password(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
			EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="loginPassword"]')))

	def checkbox_remember(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
			EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="rememberMe"]')))

	def button_forget_password(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
			EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="forgottenPassword"]')))

	def button_view_password(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
			EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="viewPw"]')))

	def button_login(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
			EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="loginButton"]')))

	def button_register(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
			EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="toRegistration"]')))

	def error_message_username(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
			EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="errorUsername"]')))

	def error_message_password(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
			EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="errorPassword"]')))

	def alert_message(self):
		alert = WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.alert_is_present())
		text = alert.text
		alert.accept()
		return text
