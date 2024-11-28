from pytest import mark
from LIBRARY.lib import Generic_code
from POM.Login import Login_Page
from POM.Home_page import Demo_Home_page
# data=("mail,pwd",[("xyz@universe.com","xyz@123")])

@mark.parametrize("mail, pwd", [("xyz@universe.com", "xyz@123"),("abc@universe.com","abc@123")])
def test_login(_driver,mail,pwd):
    # s=Generic_code(_driver)
    home_page=Demo_Home_page(_driver)
    home_page.click_login()
    loginpage=Login_Page(_driver)
    loginpage.login(mail,pwd)
    logged_in_user_element = _driver.find_element("xpath", "//a[@class='ico-logout']")
    assert logged_in_user_element.is_displayed(), "Login failed, logout button not found."

@mark.parametrize("mail, pwd", [("ab@universe.com", "xyz@123"),("aq@universe.com","abc@123")])
def test_invalid_login(_driver,mail,pwd):
    s=Generic_code(_driver)
    home_page=Demo_Home_page(_driver)
    home_page.click_login()
    loginpage=Login_Page(_driver)
    loginpage.login(mail,pwd)
    error_message=_driver.find_element("xpath",'//div[@class="validation-summary-errors"]')
    assert  error_message.is_displayed(),"Login was unsuccessful. Please correct the errors and try again."