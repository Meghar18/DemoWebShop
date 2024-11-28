from LIBRARY.lib import Generic_code
from LIBRARY.Excel import read_locators

class Demo_Home_page:
    _locators=read_locators("homepage")
    def __init__(self,driver):
        self.driver=driver

    def click_register(self):
        s=Generic_code(self.driver)
        s.click_element(self._locators["lnk_register"])

    def click_login(self):
        s=Generic_code(self.driver)
        s.click_element(self._locators["lnk_login"])

    def click_shopping_cart(self):
        s=Generic_code(self.driver)
        s.click_element(self._locators["lnk_shopping_cart"])

    def click_wish_list(self):
        s=Generic_code(self.driver)
        s.click_element(self._locators["lnk_wish_list"])
