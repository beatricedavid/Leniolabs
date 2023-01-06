import unittest
from selenium import webdriver

class SetupWeb(unittest.TestCase):

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.close()
    driver.quit()