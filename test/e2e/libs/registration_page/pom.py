from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ..basics.general_model import GeneralPage

DEFAULT_TIMEOUT = 10

class RegistrationPage(GeneralPage):

    def __init__(self, driver: webdriver.Chrome):
        self.url = 'http://ec2-13-60-30-176.eu-north-1.compute.amazonaws.com/#/user-registration'
        super().__init__(driver, self.url)

    def input_username(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="InputUsername"]')))

    def input_email(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="InputEmail"]')))

    def input_password(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="InputPassword"]')))

    def button_view_password(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="viewPw"]')))

    def input_confirm_password(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="InputConfirmPassword"]')))

    def button_view_confirm_password(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="viewPw2"]')))

    def checkbox_terms(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="CheckBoxTerms"]')))

    def button_terms(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="linkGTC"]')))

    def button_submit(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="ButtonSubmit"]')))

    def button_return_to_login(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="returnToLogin"]')))

    def input_first_name(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="InputFirstName"]')))

    def input_last_name(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="InputLastName"]')))

    def input_phone_number(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="InputPhoneNumber"]')))

    def error_message_username(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="ErrorUsername"]')))

    def error_message_first_name(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="ErrorFirstName"]')))

    def error_message_email(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="ErrorEmail"]')))

    def error_message_last_name(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="ErrorLastName"]')))

    def error_message_phone_number(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="ErrorPhoneNr"]')))

    def error_message_password(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="ErrorPassword"]')))

    def error_message_password_confirm(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="errorConfirmPassword"]')))
