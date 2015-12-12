import getpass
from selenium.webdriver.common.keys import Keys

def login(driver, username="", password=""):
    if "Login" in driver.title:
        try:
            
            # username
            elem = driver.find_element_by_id("MyMatrix_ctl06_ctl06_txtLogin")
            if (username == ""):
                print("username: ", end="")
                username = input()
            elem.send_keys(username)
            
            # password
            elem = driver.find_element_by_id("MyMatrix_ctl06_ctl06_txtPwd")
            if (password == ""):
                password = getpass.getpass("password for " + username + ": ")
            elem.send_keys(password)
            
            # login
            elem.send_keys(Keys.RETURN)

            # validate correct login
            if "Login" in driver.title:
                return "An error occurred in function login(): bad login?"

            # log in sucessfull
            return driver

        # something happen
        except Exception as e:
            return "An error occurred in function login(): bad login?"

    # this is not the login page
    return "An error occurred in function login(): wrong page?"

def navigate(driver, page):
    try:
        el = driver.find_element_by_link_text(page)
        el.click()
        return driver
    except Exception as e:
        return "An error occurred in function navigate(): sure link '" + page + "' exists?"
        
