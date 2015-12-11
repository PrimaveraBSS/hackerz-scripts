import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import json

## load data
with open("time-report.json") as data_file:
    data = json.load(data_file)

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
password = getpass.getpass("password for " + username + ": ")
elem.send_keys(password)
# login
elem.send_keys(Keys.RETURN)

## navigate to time report page
assert "My Initiative Management" in driver.title
elem = driver.find_element_by_link_text("Time Report")
elem.send_keys(Keys.RETURN)

## navigate to time report page
assert "My Initiative Management" in driver.title
elem = driver.find_element_by_link_text("Time Report")
elem.send_keys(Keys.RETURN)

## time report
assert "Time Report" in driver.title
for times in data["time"]:
    # verifica se esta no dia a reportar
    elem = driver.find_element_by_id("MyMatrix_ctl07_lblEditarDia")
    if not elem.text == "Editar Dia: " + times["dia"]:
        
        # move pare o ano a reportar
        while (times["dia"].split("-")[2] != elem.text.replace("Editar Dia: ", "").split("-")[2]):
            if (times["dia"].split("-")[2] > elem.text.replace("Editar Dia: ", "").split("-")[2]):
                # ano a reportar maior que ano posicionado, move para a direita
                elem = driver.find_element_by_id("MyMatrix_ctl07_wcReportacaoHoras_502")
                elem.click()
            else:
                # ano a reportar menor que ano posicionado, move para a esquerda
                elem = driver.find_element_by_id("MyMatrix_ctl07_wcReportacaoHoras_500")
                elem.click()

            elem = driver.find_element_by_id("MyMatrix_ctl07_wcReportacaoHoras_512")
            elem.find_elements_by_class_name("date_day")[0].click()
            elem = driver.find_element_by_id("MyMatrix_ctl07_lblEditarDia")

            
        # move pare o mes a reportar
        while (times["dia"].split("-")[1] != elem.text.replace("Editar Dia: ", "").split("-")[1]):
            if (times["dia"].split("-")[1] > elem.text.replace("Editar Dia: ", "").split("-")[1]):
                # mes a reportar maior que mes posicionado, move para a direita
                elem = driver.find_element_by_id("MyMatrix_ctl07_wcReportacaoHoras_502")
                elem.click()
            else:
                # mes a reportar menor que mes posicionado, move para a esquerda
                elem = driver.find_element_by_id("MyMatrix_ctl07_wcReportacaoHoras_500")
                elem.click()

            elem = driver.find_element_by_id("MyMatrix_ctl07_wcReportacaoHoras_512")
            elem.find_elements_by_class_name("date_day")[0].click()
            elem = driver.find_element_by_id("MyMatrix_ctl07_lblEditarDia")

    # seleciona o dia
    elem = driver.find_element_by_id("MyMatrix_ctl07_wcReportacaoHoras_512")
    elem = elem.find_elements_by_class_name("date_day")
    for dayElem in elem:
        if dayElem.text == times["dia"].split("-")[0]:
            dayElem.click()
            break

    # verfica se não tem report neste dia
    elem = driver.find_element_by_id("MyMatrix_ctl07_txtTotalHoras")
    if (elem.get_attribute("value") != "0"): # tem horas reportas, passa em frente
        continue

    # seleciona o projecto
    select = Select(driver.find_element_by_id("MyMatrix_ctl07_ddlProject"))
    select.select_by_visible_text(times["projecto"])
    # seleciona a actividade
    select = Select(driver.find_element_by_id("MyMatrix_ctl07_ddlActivity"))
    select.select_by_visible_text(times["actividade"])
    # marca as horas
    elem = driver.find_element_by_id("MyMatrix_ctl07_txtHours")
    elem.send_keys(times["horas"])

    # grava o report
    elem = driver.find_element_by_id("MyMatrix_ctl07_btnGravar")
    elem.click()
    
driver.close()
