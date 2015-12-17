def loadJsonData(file):
    import json

    ## load data
    with open(file, encoding="utf-8") as data_file:
        raw_data = json.load(data_file)


    data = {"login": {}, "time": []}
    # login data
    if "username" in raw_data["login"]:
        data["login"]["username"] = raw_data["login"]["username"]
    if "password" in raw_data["login"]:
        data["login"]["password"] = raw_data["login"]["password"]

    #
    # times
    #

    time_id = 0
    static = raw_data["static"]
    for time in raw_data["time"]:

        # mandatory fields
        # only field that cannot be static
        if "dia" not in time:
            raise ValueError("Campo dia não encontrado em time[" + str(time_id) + "]")
        if "projecto" not in time and "projecto" not in static:
            raise ValueError("Campo projecto não encontrado em time[" + str(time_id) + "]")
        if "actividade" not in time and "actividade" not in static:
            raise ValueError("Campo actividade não encontrado em time[" + str(time_id) + "]")
        if "horas" not in time and "horas" not in static:
            raise ValueError("Campo horas não encontrado em time[" + str(time_id) + "]")
        data["time"].append({
            "dia": time["dia"],
            "projecto": time["projecto"] if "projecto" in time else static["projecto"],
            "actividade": time["actividade"] if "actividade" in time else static["actividade"],
            "horas": time["horas"] if "horas" in time else static["horas"]
        })

        # optional fields
        if "comentario" in time and "comentario" not in static:
            data["time"][time_id]["comentario"] = time["comentario"] if "comentario" in time else static["comentario"]
        if "expenses" in time:
            data["time"][time_id]["expenses"] = []
            expense_id = 0
            for expense in time["expenses"]:

                #
                # expenses
                #

                # mandatory fields
                if "tipo" not in expense and "tipo" not in static["expenses"]:
                    raise ValueError("Campo tipo não encontrado em time["
                                     + str(time_id) + "][\"expenses\"]["
                                     + str(expense_id) + "]")
                if "local" not in expense and "local" not in static["expenses"]:
                    raise ValueError("Campo local não encontrado em time["
                                     + str(time_id) + "][\"expenses\"]["
                                     + str(expense_id) + "]")
                if "moeda" not in expense and "moeda" not in static["expenses"]:
                    raise ValueError("Campo moeda não encontrado em time["
                                     + str(time_id) + "][\"expenses\"]["
                                     + str(expense_id) + "]")
                if "valor" not in expense and "valor" not in static["expenses"]:
                    raise ValueError("Campo valor não encontrado em time["
                                     + str(time_id) + "][\"expenses\"]["
                                     + str(expense_id) + "]")
                expenseType = expense["tipo"] if "tipo" in expense else static["expenses"]["tipo"]
                if expenseType == "Kms in proper car":
                    if "itenerario" not in expense and "itenerario" not in static["expenses"]:
                        raise ValueError("Campo itenerario não encontrado em time["
                                         + str(time_id) + "][\"expenses\"]["
                                         + str(expense_id) + "]")
                    if "diaDeslocao" not in expense and "diaDeslocao" not in static["expenses"]:
                        raise ValueError("Campo diaDeslocao não encontrado em time["
                                         + str(time_id) + "][\"expenses\"]["
                                         + str(expense_id) + "]")
                    if "kms" not in expense and "kms" not in static["expenses"]:
                        raise ValueError("Campo kms não encontrado em time["
                                         + str(time_id) + "][\"expenses\"]["
                                         + str(expense_id) + "]")
                    if "proposito" not in expense and "proposito" not in static["expenses"]:
                        raise ValueError("Campo proposito não encontrado em time["
                                         + str(time_id) + "][\"expenses\"]["
                                         + str(expense_id) + "]")
                flags = {"Diesel", "Gasoline", "Islands-Gasoline", "Kms in proper car", "Parking", "Tolls gate"}
                if expenseType in flags:
                    if "matricula" not in expense and "matricula" not in static["expenses"]:
                        raise ValueError("Campo matricula não encontrado em time["
                                         + str(time_id) + "][\"expenses\"]["
                                         + str(expense_id) + "]")
                flags = {"Mobility", "Night Out"}
                if expenseType in flags:
                    if "regiao" not in expense and "regiao" not in static["expenses"]:
                        raise ValueError("Campo regiao não encontrado em time["
                                         + str(time_id) + "][\"expenses\"]["
                                         + str(expense_id) + "]")
                data["time"][time_id]["expenses"].append({
                    "tipo": expense["tipo"] if "tipo" in expense else static["expenses"]["tipo"],
                    "local": expense["local"] if "local" in expense else static["expenses"]["local"],
                    "moeda": expense["moeda"] if "moeda" in expense else static["expenses"]["moeda"],
                    "valor": expense["valor"] if "valor" in expense else static["expenses"]["valor"]
                })
                if "itenerario" in expense and "itenerario" not in static["expenses"]:
                    data["time"][time_id]["expenses"][expense_id]["itenerario"] = expense["itenerario"] if "itenerario" in expense else static["expenses"][""]
                if "diaDeslocao" in expense and "diaDeslocao" not in static["expenses"]:
                    data["time"][time_id]["expenses"][expense_id]["diaDeslocao"] = expense["diaDeslocao"] if "diaDeslocao" in expense else static["expenses"][""]
                if "kms" in expense and "kms" not in static["expenses"]:
                    data["time"][time_id]["expenses"][expense_id]["kms"] = expense["kms"] if "kms" in expense else static["expenses"][""]
                if "proposito" in expense and "proposito" not in static["expenses"]:
                    data["time"][time_id]["expenses"][expense_id]["proposito"] = expense["proposito"] if "proposito" in expense else static["expenses"][""]
                if "matricula" in expense and "matricula" not in static["expenses"]:
                    data["time"][time_id]["expenses"][expense_id]["matricula"] = expense["matricula"] if "matricula" in expense else static["expenses"][""]
                if "regiao" in expense and "regiao" not in static["expenses"]:
                    data["time"][time_id]["expenses"][expense_id]["regiao"] = expense["regiao"] if "regiao" in expense else static["expenses"][""]

                # optional fields
                if "observacoes" in expense and "observacoes" not in static["expenses"]:
                    data["time"][time_id]["expenses"][expense_id]["observacoes"] = expense["observacoes"] if "observacoes" in expense else static["expenses"][""]

                expense_id += 1
        
        time_id += 1

    return data
