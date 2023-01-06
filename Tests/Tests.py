from Config.SetupWeb import SetupWeb
from Pages.LoginPage import LoginPage
from Pages.SecureAreaPage import SecureAreaPage


class Tests(SetupWeb):

    def test_login_ok(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enter_user("tomsmith")
        self.loginPage.enter_password("SuperSecretPassword!")
        self.loginPage.press_login()
        self.assertEqual(self.loginPage.get_title(), "Secure Area")

    def test_login_NoOk(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enter_user("tomsmith")
        self.loginPage.enter_password("wrongpassword")
        self.loginPage.press_login()
        self.assertIn("Your password is invalid!", self.loginPage.get_alert_txt())


    def test_logout(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enter_user("tomsmith")
        self.loginPage.enter_password("SuperSecretPassword!")
        self.loginPage.press_login()
        self.secureAreaPage = SecureAreaPage(self.driver)
        self.secureAreaPage.press_logout()
        self.assertIn("You logged out of the secure area!", self.loginPage.get_message_logout_ok())