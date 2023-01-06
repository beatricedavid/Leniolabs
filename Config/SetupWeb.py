import unittest
from selenium import webdriver

class SetupWeb(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://the-internet.herokuapp.com/login")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()