from LIBRARY.lib import Generic_code
from POM.Home_page import Demo_Home_page
from LIBRARY.Excel import read_locators

class Login_Page:
    _locators=read_locators("login")
    def __init__(self,driver):
        self.driver=driver

    def login(self,email,password):
        s=Generic_code(self.driver)
        homepage=Demo_Home_page(self.driver)
        homepage.click_login()
        s.enter_text(self._locators["text_login_email"],value=email)
        s.enter_text(self._locators["text_login_pwd"],value=password)
        # s.click_element(self._locators["link_login"])
        if "link_login" in self._locators:
            s.click_element(self._locators["link_login"])
        else:
            print("Key 'link_login' not found in locators!")