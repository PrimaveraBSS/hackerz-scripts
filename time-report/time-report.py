import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import json
import getpass
from time import sleep
from validatejson import loadJsonData

#
#
#
def moveToDate(driver, calendar, date):
    cldr_acts = {
        "report": {},
        "expenses": {}
    }
    cldr_acts["report"] = {
        "mv_lft": "MyMatrix_ctl07_wcReportacaoHoras_500",
        "mv_rht": "MyMatrix_ctl07_wcReportacaoHoras_502",
        "dy_pck": "MyMatrix_ctl07_wcReportacaoHoras_512",
        "dy_lbl": "MyMatrix_ctl07_lblEditarDia",
        "dy_lbl_start": "Editar Dia: "
    }
    cldr_acts["expenses"] = {
        "mv_lft": "MyMatrix_ctl07_wcRegistoDespesas_500",
        "mv_rht": "MyMatrix_ctl07_wcRegistoDespesas_502",
        "dy_pck": "MyMatrix_ctl07_wcRegistoDespesas_512",
        "dy_lbl": "MyMatrix_ctl07_lblTitulo",
        "dy_lbl_start": "Despesas para o dia: "
    }

    # verifica se esta no dia a reportar
    elem = driver.find_element_by_id(cldr_acts[calendar]["dy_lbl"])
    if not elem.text == cldr_acts[calendar]["dy_lbl_start"] + date:
        
        # move pare o ano a reportar
        while (date.split("-")[2] != elem.text.replace(cldr_acts[calendar]["dy_lbl_start"], "").split("-")[2]):
            if (date.split("-")[2] > elem.text.replace(cldr_acts[calendar]["dy_lbl_start"], "").split("-")[2]):
                # ano a reportar maior que ano posicionado, move para a direita
                elem = driver.find_element_by_id(cldr_acts[calendar]["mv_rht"])
                elem.click()
            else:
                # ano a reportar menor que ano posicionado, move para a esquerda
                elem = driver.find_element_by_id(cldr_acts[calendar]["mv_lft"])
                elem.click()

            elem = driver.find_element_by_id(cldr_acts[calendar]["dy_pck"])
            elem.find_elements_by_class_name("date_day")[0].click()
            elem = driver.find_element_by_id(cldr_acts[calendar]["dy_lbl"])

            
        # move pare o mes a reportar
        while (date.split("-")[1] != elem.text.replace(cldr_acts[calendar]["dy_lbl_start"], "").split("-")[1]):
            if (date.split("-")[1] > elem.text.replace(cldr_acts[calendar]["dy_lbl_start"], "").split("-")[1]):
                # mes a reportar maior que mes posicionado, move para a direita
                elem = driver.find_element_by_id(cldr_acts[calendar]["mv_rht"])
                elem.click()
            else:
                # mes a reportar menor que mes posicionado, move para a esquerda
                elem = driver.find_element_by_id(cldr_acts[calendar]["mv_lft"])
                elem.click()

            elem = driver.find_element_by_id(cldr_acts[calendar]["dy_pck"])
            elem.find_elements_by_class_name("date_day")[0].click()
            elem = driver.find_element_by_id(cldr_acts[calendar]["dy_lbl"])

    # seleciona o dia
    elem = driver.find_element_by_id(cldr_acts[calendar]["dy_pck"])
    elem = elem.find_elements_by_class_name("date_day")
    for dayElem in elem:
        if dayElem.text == date.split("-")[0]:
            dayElem.click()
            break

## load data
data = loadJsonData("time-report.json")
# ask for credentials imediatly
# username
if "username" in data["login"]:
    username = data["login"]["username"]
else:
    print("username: ", end="")
    username = input()
# password
if "password" in data["login"]:
    password = data["login"]["password"]
else:
    password = getpass.getpass("password for " + username + ": ")


# start browser automation
driver = webdriver.Chrome()

try:
    ## Login
    driver.get("http://www.primaverabss.com/consultingspace/Home%20Page-Login.aspx")
    assert "Login" in driver.title
    # username
    elem = driver.find_element_by_id("MyMatrix_ctl06_ctl06_txtLogin")
    elem.send_keys(username)
    # password
    elem = driver.find_element_by_id("MyMatrix_ctl06_ctl06_txtPwd")
    elem.send_keys(password)
    # login
    elem.send_keys(Keys.RETURN)
    assert "My Initiative Management" in driver.title

    ## Integrate all approved expense notes
    elem = driver.find_element_by_link_text("Expenses Report")
    elem.send_keys(Keys.RETURN)
    assert "Expenses Report" in driver.title
    elem = driver.find_element_by_id("MyMatrix_ctl07_btnIntegrarDAF")
    elem.click()

    ## navigate to time repor4t page
    elem = driver.find_element_by_link_text("Time Report")
    elem.send_keys(Keys.RETURN)
    assert "Time Report" in driver.title

    ## time report
    for times in data["time"]:
        moveToDate(driver, "report", times["dia"])

        # verfica se não tem report neste dia
        elem = driver.find_element_by_id("MyMatrix_ctl07_txtTotalHoras")
        if (elem.get_attribute("value") != "0"): # tem horas reportas, passa em frente
            continue

        # projecto
        select = Select(driver.find_element_by_id("MyMatrix_ctl07_ddlProject"))
        select.select_by_visible_text(times["projecto"])
        
        # actividade
        select = Select(driver.find_element_by_id("MyMatrix_ctl07_ddlActivity"))
        select.select_by_visible_text(times["actividade"])
        
        # horas
        elem = driver.find_element_by_id("MyMatrix_ctl07_txtHours")
        elem.send_keys(times["horas"])

        # comentario
        if "comentario" in times:  
            elem = driver.find_element_by_id("MyMatrix_ctl07_txtComment")
            elem.send_keys(times["comentario"])

        # grava o report, passa ao próximo
        elem = driver.find_element_by_id("MyMatrix_ctl07_btnGravar")
        elem.click()

        # reporta despesas
        expenseIds = []
        if "expenses" in times:
            # navigate to expense page 
            elem = driver.find_element_by_link_text("Expenses Report")
            elem.send_keys(Keys.RETURN)
            assert "Expenses Report" in driver.title
                
            for expense in times["expenses"]:
                moveToDate(driver, "expenses", times["dia"])

                # tipo
                select = Select(driver.find_element_by_id("MyMatrix_ctl07_ddlTipoDespesa"))
                select.select_by_visible_text(expense["tipo"])

                # local
                select = Select(driver.find_element_by_id("MyMatrix_ctl07_ddlLocal"))
                select.select_by_visible_text(expense["local"])

                # specifics
                tipos = {"Diesel", "Gasoline", "Islands-Gasoline", "Kms in proper car", "Parking", "Tolls gate"}
                if expense["tipo"] in tipos:
                    # matricula
                    elem = driver.find_element_by_id("MyMatrix_ctl07_txtMatriculaOnly")
                    elem.send_keys(expense["matricula"])

                tipos = {"Kms in proper car"}
                if expense["tipo"] in tipos:
                    # itenerario
                    elem = driver.find_element_by_id("MyMatrix_ctl07_txtDeslocacao")
                    elem.send_keys(expense["itenerario"])
                    
                    # diaDeslocao
                    elem = driver.find_element_by_id("MyMatrix_ctl07_txtDiaDeslocacao")
                    elem.send_keys(expense["diaDeslocao"])
                    
                    # kms
                    elem = driver.find_element_by_id("MyMatrix_ctl07_txtKms")
                    elem.send_keys(expense["kms"])
                    
                    # proposito
                    elem = driver.find_element_by_id("MyMatrix_ctl07_txtCausas")
                    elem.send_keys(expense["proposito"])

                tipos = {"Mobility", "Night Out"}
                if expense["tipo"] in tipos:
                    # regiao
                    select = Select(driver.find_element_by_id("MyMatrix_ctl07_ddlRegiao"))
                    select.select_by_visible_text(expense["regiao"])
                    
                # valor !should not be last, otherwise selenium won't wait for exchange recal!
                elem = driver.find_element_by_id("MyMatrix_ctl07_txtValorOriginal")
                elem.clear()
                elem = driver.find_element_by_id("MyMatrix_ctl07_txtValorOriginal")
                elem.send_keys(expense["valor"])

                # observacoes
                if "observacoes" in expense:
                    elem = driver.find_element_by_id("MyMatrix_ctl07_txtObservacoes")
                    elem.send_keys(expense["observacoes"])

                # moeda
                select = Select(driver.find_element_by_id("MyMatrix_ctl07_ddlMoeda"))
                select.select_by_visible_text(expense["moeda"])

                # gravar                
                elem = driver.find_element_by_id("MyMatrix_ctl07_btnGravar")
                elem.click()

                # devolver id da despesa inserida
                table = driver.find_element_by_id("MyMatrix_ctl07_GridView")
                table = table.find_element_by_tag_name("tbody")
                tableRows = table.find_elements_by_tag_name("tr")
                for tableRow in tableRows:
                    try:
                        tableRowData = tableRow.find_element_by_tag_name("td")
                    except NoSuchElementException:
                        continue
                    if tableRowData.text != " " and tableRowData.text not in expenseIds:
                        expenseIds.append(tableRowData.text)
                        print(tableRowData.text + " " + times["dia"] + " " + expense["tipo"] + " " + expense["valor"])
            

            ## navigate back to time report page
            elem = driver.find_element_by_link_text("Time Report")
            elem.send_keys(Keys.RETURN)

finally:
    # close driver and exit
    driver.close()
