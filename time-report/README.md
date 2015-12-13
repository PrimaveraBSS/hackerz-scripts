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
                "horas": "7|3.5",
				"comentario": ".*"
				"expenses": [
					"tipo": "Another Meal|Diesel|Gasoline|Hotels|Islands-Another meal|Islands-Gasoline|Islands-Lunch working day|Islands-Taxis|Kms in proper car|Lunch working Day|Mobility|Night Out|Other Expenses (detail)|Parking|Taxi Primavera (Sr. Marco)|Taxis|Tolls gate",
					"local": "Ilhas Açores|Ilhas Madeira|Intracomunitário Espanha|Intracomunitário Outros|Nacional|Outros Mercados",
					"itenerario": ".*",
					"diaDeslocao": ".*",
					"kms": ".*",
					"proposito": ".*",
					"matricula": ".*",
					"regiao": "Outros|ROA|ES|AO|MZ|PT",
					"moeda": "AED|AZK|CVE|EUR|MZN|USD",
					"valor": "[\d]+.[\d]{2}",
					"observacoes": ".*"
				]
            }
        ]
    }

#### Campos

`login`.`username`: O nome de login no IM (se omitido será pedido na consola)

`login`.`password`: A senha de login no IM (se omitido será pedido na consola)

`time`: lista de tempos e despesas associadas a reportar

`time`.`dia`: Dia a reportar no exacto formato que está no IM. Deve validar com a expressão regular `[\d]{1,2}-[\d]{1,2}-[\d]{4}`

`time`.`projecto`: Nome do projecto a reportar, exactamente como fica visível na combobox do site (usa `time-report-activity-list.py` para obter uma lista de projectos disponíveis)

`time`.`actividade`: Nome da actividade a reportar, exactamente como fica visível na combobox do site (usa `time-report-activity-list.py` para obter uma lista de actividades disponíveis para cada projecto)

`time`.`horas`: 7 ou 3.5, conforme especificação da CSU

`time`.`expenses`: lista de despesas a reportar para o dia

`time`.`expenses`.`tipo`: Tipo da despesa, exactamente como fica visível na combobox do site

`time`.`expenses`.`local`: Local da despesa exactamente como fica visível na combobox do site

`time`.`expenses`.`itenerario`: Disponível apenas para o tipo 'Kms in proper car'

`time`.`expenses`.`diaDeslocao`: Disponível apenas para o tipo 'Kms in proper car'

`time`.`expenses`.`kms`: Disponível apenas para o tipo 'Kms in proper car'

`time`.`expenses`.`proposito`: Disponível apenas para o tipo 'Kms in proper car'

`time`.`expenses`.`matricula`: Disponível apenas para os tipos 'Diesel', 'Gasoline', 'Islands-Gasoline', 'Kms in proper car', 'Parking', 'Tolls gate'

`time`.`expenses`.`regiao`:  Disponível apenas para os tipos 'Mobility', 'Night Out'

`time`.`expenses`.`moeda`: Moeda da despesa

`time`.`expenses`.`valor`: Valor original da despesa

`time`.`expenses`.`observacoes`: (Opcional) Obsercações da despesa
