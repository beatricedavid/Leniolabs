from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.user_txt = "username"
        self.pass_txt = "password"
        self.login_button = "//i[@class='fa fa-2x fa-sign-in']"
        self.title_txt = "//h2[normalize-space()='Secure Area']"
        self.alertWrongCred = "flash"
        self.messageLogoutOk = "flash"

    def enter_user(self, user):
        self.driver.find_element(By.ID, self.user_txt).send_keys(user)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.pass_txt).send_keys(password)

    def press_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def get_title(self):
        WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, self.title_txt)))
        title = self.driver.find_element(By.XPATH, self.title_txt).text
        return title

    def get_alert_txt(self):
        alert_txt = self.driver.find_element(By.ID, self.alertWrongCred).text
        return alert_txt

    def get_message_logout_ok(self):
        message_ok_logout = self.driver.find_element(By.ID, self.messageLogoutOk).text
        return message_ok_logout