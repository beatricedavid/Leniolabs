from selenium.webdriver.common.by import By

class SecureAreaPage:

    def __init__(self, driver):
        self.driver = driver
        self.title_txt = ".button.secondary.radius"


    def press_logout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.title_txt).click()
