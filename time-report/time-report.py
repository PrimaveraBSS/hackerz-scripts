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
    print("selecting " + times["dia"])
    # select day, navigating if necessary
    calendar = "report"
    catch = navigateToDate(driver, "report", times["dia"])
    if type(catch) is str:
        driver.close()
        print(catch)
        sys.exit()

##    # verfica se não tem report neste dia
##    elem = driver.find_element_by_id("MyMatrix_ctl07_txtTotalHoras")
##    if (elem.get_attribute("value") != "0"): # tem horas reportas, passa em frente
##        continue
##
##    # seleciona o projecto
##    select = Select(driver.find_element_by_id("MyMatrix_ctl07_ddlProject"))
##    select.select_by_visible_text(times["projecto"])
##    # seleciona a actividade
##    select = Select(driver.find_element_by_id("MyMatrix_ctl07_ddlActivity"))
##    select.select_by_visible_text(times["actividade"])
##    # marca as horas
##    elem = driver.find_element_by_id("MyMatrix_ctl07_txtHours")
##    elem.send_keys(times["horas"])
##
##    # grava o report, passa ao próximo ou fecha o browser
##    elem = driver.find_element_by_id("MyMatrix_ctl07_btnGravar")
##    #elem.click()
    
driver.close()
