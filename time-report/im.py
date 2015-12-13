import getpass
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import re
import time

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

def navigateToLink(driver, page):
    try:
        
        el = driver.find_element_by_link_text(page)
        el.click()
        
        return driver
    except Exception as e:
        return "An error occurred in function navigateToLink(): sure link '" + page + "' exists?"

def navigateToDate(driver, calendar, date):
    try:

        calendar_actions = {
            "report": {},
            "planning": {}
        }
        calendar_actions["report"] = {
            "move_left": "MyMatrix_ctl07_wcReportacaoHoras_500",
            "move_right": "MyMatrix_ctl07_wcReportacaoHoras_502",
            "day_picker": "MyMatrix_ctl07_wcReportacaoHoras_512"
        }
        calendar_actions["planning"] = {
            "move_left": "MyMatrix_ctl07_wcPlaneamento_500",
            "move_right": "MyMatrix_ctl07_wcPlaneamento_502",
            "day_picker": "MyMatrix_ctl07_wcPlaneamento_512"
        }

        # check year, by picking a day
        currentDate = __touchDayOne(driver, calendar_actions[calendar]["day_picker"])
        while (currentDate.group("ano") != date.split("-")[2]):
            # move
            direction = "move_left" if (currentDate.group("ano") > date.split("-")[2]) else "move_right"
            driver.find_element_by_id(calendar_actions[calendar][direction]).click()
            # recap
            currentDate = __touchDayOne(driver, calendar_actions[calendar]["day_picker"])

        while (currentDate.group("mes") != date.split("-")[1]):
            # move
            direction = "move_left" if (currentDate.group("mes") > date.split("-")[1]) else "move_right"
            driver.find_element_by_id(calendar_actions[calendar][direction]).click()
            # recap
            currentDate = __touchDayOne(driver, calendar_actions[calendar]["day_picker"])

        # pick day
        days = driver.find_element_by_id(calendar_actions[calendar]["day_picker"])
        days = days.find_elements_by_class_name("date_day")
        for day in days:
            if day.text == date.split("-")[0]:
                day.click()
                break
        
    except Exception as e:
        return "An error occurred in function navigateToDate(): sure day '" + date + "' exists?"

def isDayApproved(driver, date):
    try:

        # navigate to date
        catch = navigateToDate(driver, "report", date)
        if type(catch) is str:
            return " isDayApproved() -> " + catch

        # check if element 'Aprovado' exists
        try:
            driver.find_element_by_id("MyMatrix_ctl07_lblAprovado")
        except NoSuchElementException:
            return False

        # reached here so element does exists
        return True

    except Exception as e:
        return "An error occurred in function isDayApproved(): " + e


def __touchDayOne(driver, element_id):
    # find and touch first day
    days = driver.find_element_by_id(element_id)
    days.find_elements_by_class_name("date_day")[0].click()
    # regex parse the date
    currentDate = re.compile(r".*: (?P<dia>[\d]{1,2})-(?P<mes>[\d]{1,2})-(?P<ano>[\d]{4})")
    return currentDate.search(driver.find_element_by_id("MyMatrix_ctl07_lblEditarDia").text)
