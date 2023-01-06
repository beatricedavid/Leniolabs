from appium import webdriver
import unittest

class SetupApp(unittest.TestCase):

    caps = {
        'platformName': 'android',
        'deviceName': 'Galaxy-s20-David',
        'automationName': 'UIAutomator2',
        'appPackage': 'com.runtastic.android',
        'appActivity': '.activities.StartActivity',
    }
    AppiumDriver = webdriver.Remote(desired_capabilities=caps, command_executor="http://127.0.0.1:4723/wd/hub")
    AppiumDriver.quit()