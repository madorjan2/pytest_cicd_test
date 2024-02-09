from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_preconfigured_chrome_driver(headless=True) -> webdriver.Chrome:
    options = Options()
    options.add_experimental_option('detach', True)
    if headless:
        options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    return driver
