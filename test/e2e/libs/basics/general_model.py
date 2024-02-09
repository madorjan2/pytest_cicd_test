from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10
class GeneralPage:

    def __init__(self, driver: webdriver.Chrome, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def get_url(self):
        return self.driver.current_url

    def button_home_navbar(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="toHome"]')))

    def button_ad_search_navbar(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="searchProperty"]')))

    def button_loan_calc_navbar(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="loanCalculator"]')))

    def button_ad_list_navbar(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="sendAd"]')))

    def button_login_navbar(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="toLogin"]')))

