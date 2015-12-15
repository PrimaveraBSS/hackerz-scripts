def loadJsonData(file):
    import json

    ## load data
    with open(file) as data_file:
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
    for time in raw_data["time"]:

        # mandatory fields
        if "dia" not in time:
            raise ValueError("Campo dia não encontrado em time[" + str(time_id) + "]")
        if "projecto" not in time:
            raise ValueError("Campo projecto não encontrado em time[" + str(time_id) + "]")
        if "actividade" not in time:
            raise ValueError("Campo actividade não encontrado em time[" + str(time_id) + "]")
        if "horas" not in time:
            raise ValueError("Campo horas não encontrado em time[" + str(time_id) + "]")
        data["time"].append({
            "dia": time["dia"],
            "projecto": time["projecto"],
            "actividade": time["actividade"],
            "horas": time["horas"]
        })

        # optional fields
        if "comentario" in time:
            data["time"][time_id]["comentario"] = time["comentario"]
        if "expenses" in time:
            data["time"][time_id]["expenses"] = []
            expense_id = 0
            for expense in time["expenses"]:

                #
                # expenses
                #

                # mandatory fields
                if "tipo" not in expense:
                    raise ValueError("Campo tipo não encontrado em time["
                                     + str(time_id) + "][\"expenses\"]["
                                     + str(expense_id) + "]")
                if "local" not in expense:
                    raise ValueError("Campo local não encontrado em time["
                                     + str(time_id) + "][\"expenses\"]["
                                     + str(expense_id) + "]")
                if "moeda" not in expense:
                    raise ValueError("Campo moeda não encontrado em time["
                                     + str(time_id) + "][\"expenses\"]["
                                     + str(expense_id) + "]")
                if "valor" not in expense:
                    raise ValueError("Campo valor não encontrado em time["
                                     + str(time_id) + "][\"expenses\"]["
                                     + str(expense_id) + "]")
                if expense["tipo"] == "Kms in proper car":
                    if "itenerario" not in expense:
                        raise ValueError("Campo itenerario não encontrado em time["
                                         + str(time_id) + "][\"expenses\"]["
                                         + str(expense_id) + "]")
                    if "diaDeslocao" not in expense:
                        raise ValueError("Campo diaDeslocao não encontrado em time["
                                         + str(time_id) + "][\"expenses\"]["
                                         + str(expense_id) + "]")
                    if "kms" not in expense:
                        raise ValueError("Campo kms não encontrado em time["
                                         + str(time_id) + "][\"expenses\"]["
                                         + str(expense_id) + "]")
                    if "proposito" not in expense:
                        raise ValueError("Campo proposito não encontrado em time["
                                         + str(time_id) + "][\"expenses\"]["
                                         + str(expense_id) + "]")
                flags = {"Diesel", "Gasoline", "Islands-Gasoline", "Kms in proper car", "Parking", "Tolls gate"}
                if expense["tipo"] in flags:
                    if "matricula" not in expense:
                        raise ValueError("Campo matricula não encontrado em time["
                                         + str(time_id) + "][\"expenses\"]["
                                         + str(expense_id) + "]")
                flags = {"Mobility", "Night Out"}
                if expense["tipo"] in flags:
                    if "regiao" not in expense:
                        raise ValueError("Campo regiao não encontrado em time["
                                         + str(time_id) + "][\"expenses\"]["
                                         + str(expense_id) + "]")
                data["time"][time_id]["expenses"].append({
                    "tipo": expense["tipo"],
                    "local": expense["local"],
                    "moeda": expense["moeda"],
                    "valor": expense["valor"]
                })
                if "itenerario" in time:
                    data["time"][time_id]["expenses"][expense_id]["itenerario"] = expense["itenerario"]
                if "diaDeslocao" in time:
                    data["time"][time_id]["expenses"][expense_id]["diaDeslocao"] = expense["diaDeslocao"]
                if "kms" in time:
                    data["time"][time_id]["expenses"][expense_id]["kms"] = expense["kms"]
                if "proposito" in time:
                    data["time"][time_id]["expenses"][expense_id]["proposito"] = expense["proposito"]
                if "matricula" in time:
                    data["time"][time_id]["expenses"][expense_id]["matricula"] = expense["matricula"]
                if "regiao" in time:
                    data["time"][time_id]["expenses"][expense_id]["regiao"] = expense["regiao"]

                # optional fields
                if "observacoes" in time:
                    data["time"][time_id]["expenses"][expense_id]["observacoes"] = expense["observacoes"]

                expense_id += 1
        
        time_id += 1

    return data
