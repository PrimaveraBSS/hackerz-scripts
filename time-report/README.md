## Ficheiro de configuração

### Campos

#### Obrigatórios

##### Tempos

* `dia`
* `projecto`
* `actividade`
* `horas`
  * '0'
    * `comentario`

##### Despesas

* `local`
* `moeda`
* `valor`
* `tipo`
  * 'Kms in proper car'
    * `itenerario`
    * `diaDeslocao`
    * `kms`
    * `proposito`
    * `matricula`
  * 'Diesel', 'Gasoline', 'Islands-Gasoline', 'Parking', ou 'Tolls gate''
    * `matricula`
  * 'Mobility' ou 'Night Out'
    * `regiao`

#### Opcionais

##### Login

* `username` Username do IM
* `password` Password do IM

##### Tempos

* `comentario`
* `expenses`

##### Despesas

* `observacoes`

#### Estáticos

Todos os campos não compostos (não delimitados por `[` `]`), com excepção do campo `dia`, podem ter definidos valores estáticos que serão aplicados a todos os reports

Por exemplo, no report de despesas para Angola a moeda será sempre 'AKZ', podemos então definir este campo como estático e suprimí-lo em qualquer dia.

Mesmo tendo definido um valor estático, este só é utilizado em último recurso sendo dada prioridade ao campo mais especifico

	

### Estrutura

    {
        "login": {
            "username": ".*",
            "password": ".*"
        },
		"static": {
			"projecto": ".*",
			"actividade": ".*",
			"horas": "0|7|3.5",
			"comentario": ".*"
			"expenses": {
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
			}
		},
        "time": [
            {
                "dia": "[\d]{1,2}-[\d]{1,2}-[\d]{4}",
                "projecto": ".*",
                "actividade": ".*",
                "horas": "0|7|3.5",
				"comentario": ".*"
				"expenses": [
					{
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
					},
					{
						...
					}
				]
            },
			{
				...
			}
        ]
    }
	
Campos contidos por `[` `]` são arrays de dados, podendo ter n elementos do mesmo formato indicado para o primeiro elemento
