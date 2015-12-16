import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import json
import getpass
from validatejson import loadJsonData

## load data
data = loadJsonData("time-report.json")

driver = webdriver.Chrome()
## Login
driver.get("http://www.primaverabss.com/consultingspace/Home%20Page-Login.aspx")
assert "Login" in driver.title
# username
elem = driver.find_element_by_id("MyMatrix_ctl06_ctl06_txtLogin")
print("username: ", end="")
username = input()
elem.send_keys(username)
# password
elem = driver.find_element_by_id("MyMatrix_ctl06_ctl06_txtPwd")
password = getpass.getpass("password for " + username + ":")
elem.send_keys(password)
# login
elem.send_keys(Keys.RETURN)

## navigate to time report page
assert "My Initiative Management" in driver.title
elem = driver.find_element_by_link_text("Time Report")
elem.send_keys(Keys.RETURN)

## time report
assert "Time Report" in driver.title

## select projects one by one
elem = driver.find_element_by_id("MyMatrix_ctl07_ddlProject")
projects_elems = elem.find_elements_by_tag_name("option")
projects = []
for project_elem in projects_elems:
    projects.append(project_elem.get_attribute("text"))
result = {}
for project in projects:
    select = Select(driver.find_element_by_id("MyMatrix_ctl07_ddlProject"))
    select.select_by_visible_text(project)
    elem = driver.find_element_by_id("MyMatrix_ctl07_ddlActivity")
    activities = elem.find_elements_by_tag_name("option")
    result[project] = {}
    activity_id = 0
    for activity in activities:
        result[project][activity_id] = activity.get_attribute("text")
        activity_id += 1
with open("time-report-activity-list.json", "w", encoding="utf8") as result_file:
    json.dump(result, result_file, ensure_ascii=False, indent=4)


driver.close()
