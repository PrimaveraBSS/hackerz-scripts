import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import json
import getpass

from im import *

## load data
with open("time-report.json") as data_file:
    data = json.load(data_file)

driver = webdriver.Chrome()
driver.get("http://www.primaverabss.com/consultingspace")

# do login
catch = login(driver, "pedrorodrigues", "lp5an")
if type(catch) is str:
    driver.close()
    print(catch)
    sys.exit()

# navigate to time report page
catch = navigateToLink(driver, "Time Report")
if type(catch) is str:
    driver.close()
    print(catch)
    sys.exit()

## time report
assert "Time Report" in driver.title
for times in data["time"]:
    
    catch = isDayApproved(driver, times["dia"])
    if type(catch) is str:
        driver.close()
        print(catch)
        sys.exit()

    if (catch):
        print(times["dia"] + " is approved")
    else:
        print(times["dia"] + " is not approved")

    # exit if time report is already done
        # exit if time report is approved
    

    # if planning is created accept and exit
    

    # else report as filed
    
    
driver.close()
