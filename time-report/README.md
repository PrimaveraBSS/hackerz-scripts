## Ficheiro de configuração

### Estrutura

    {
        "login": {
            "username": ".*",
            "password": ".*"
        },
        "time": [
            {
                "dia": "[\d]{1,2}-[\d]{1,2}-[\d]{4}",
                "projecto": ".*",
                "actividade": ".*",
                "horas": "7|3.5"
            }
        ]
    }

#### Campos

`login`.`username`: O nome de login no IM (se omitido será pedido na consola)

`login`.`password`: A senha de login no IM (se omitido será pedido na consola)

`time`.`dia`: Dia a reportar no exacto formato que está no IM. Deve validar com a expressão regular `[\d]{1,2}-[\d]{1,2}-[\d]{4}`

`time`.`projecto`: Nome do projecto a reportar, exactamente como fica visível na combobox do site (usa `time-report-activity-list.py` para obter uma lista de projectos disponíveis)

`time`.`actividade`: Nome da actividade a reportar, exactamente como fica visível na combobox do site (usa `time-report-activity-list.py` para obter uma lista de actividades disponíveis para cada projecto)

`time`.`horas`: 7 ou 3.5, conforme especificação da CSU
