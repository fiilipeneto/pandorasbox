#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time
import requests
import urllib2
import json
import csv

url = "http://receitaws.com.br/v1/cnpj/"
#API only 3 requests per minute

# $ curl -X GET https://www.receitaws.com.br/v1/cnpj/30405879000112

# raw_cnpjs = ["05439635000103" , "06105362000123" , "04089570000150" , "08162032001096" , "04957650000180" , "04310390000157" , "03636036000316" , "05818764000102" , "05148728000189" , "09133730000135" , "08219855000110" , "03344935000183" , "00391234000107" , "06198573000158" , "06923835000108" , "04680660000111" , "05253499000162" , "02016821000141" , "05336545000197" , "00000000000000" , "03833018000162" , "03684175000153" , "01515934000390" , "00763832000160" , "08165642000152" , "03654119000257" , "05444853000136" , "02927956000169" , "05546877000104" , "03861512000130" , "06239190000857" , "06145774000197" , "02635522000195" , "04071245000160" , "07032886000102" , "09239073000105" , "01894253000119" , "04338716000154" , "08624998000107" , "08091674000150" , "07732587000172" , "03083916000140" , "04865228000103" , "04080345000153" , "08070508009396" , "06990011000142" , "05077129000111" , "08044854000181" , "05868574001090" , "01610798000156" , "07358931000105" , "02445414000150" , "09416648000118" , "00070596000104" , "02865831000151" , "01944380000185" , "04188086000260" , "00720437000108" , "05097311000134" , "08280681000109" , "05051620000173" , "08862665000116" , "00764452000140"]

raw_cnpjs = ["30405879000112"]

list_cnpj = []
for item in raw_cnpjs:
    list_cnpj.append(str(item))

# cnpj = ["14597970000120"]

json_example = """
{
  "atividade_principal": [
    {
      "text": "Suporte técnico, manutenção e outros serviços em tecnologia da informação",
      "code": "62.09-1-00"
    }
  ],
  "data_situacao": "18/10/2011",
  "complemento": "CONJ 603",
  "nome": "MDM SOLUCOES LTDA",
  "uf": "SP",
  "telefone": "(11) 2933-9391",
  "email": "financeiro@mdmsolutions.com.br",
  "atividades_secundarias": [
    {
      "text": "Consultoria em tecnologia da informação",
      "code": "62.04-0-00"
    },
    {
      "text": "Desenvolvimento e licenciamento de programas de computador customizáveis",
      "code": "62.02-3-00"
    },
    {
      "text": "Desenvolvimento de programas de computador sob encomenda",
      "code": "62.01-5-01"
    },
    {
      "text": "Desenvolvimento e licenciamento de programas de computador não-customizáveis",
      "code": "62.03-1-00"
    },
    {
      "text": "Comércio varejista especializado de equipamentos e suprimentos de informática",
      "code": "47.51-2-01"
    },
    {
      "text": "Aluguel de máquinas e equipamentos para escritórios",
      "code": "77.33-1-00"
    }
  ],
  "qsa": [
    {
      "qual": "49-Sócio-Administrador",
      "nome": "MARCO ANTONIO DA SILVA BOEMEKE"
    },
    {
      "qual": "22-Sócio",
      "nome": "ANDRE GHIGNATTI"
    },
    {
      "qual": "22-Sócio",
      "nome": "DANIEL LUIZ GIRARDI DIAS"
    },
    {
      "qual": "49-Sócio-Administrador",
      "nome": "VINICIUS MORALES BOEMEKE"
    },
    {
      "qual": "22-Sócio",
      "nome": "BRUNO ATRIB ZANCHET"
    }
  ],
  "situacao": "ATIVA",
  "bairro": "AGUA BRANCA",
  "logradouro": "AV FRANCISCO MATARAZZO",
  "numero": "404",
  "cep": "05.001-000",
  "municipio": "SAO PAULO",
  "abertura": "18/10/2011",
  "natureza_juridica": "206-2 - Sociedade Empresária Limitada",
  "fantasia": "MDM SOLUTIONS",
  "cnpj": "14.597.970/0001-20",
  "ultima_atualizacao": "2018-07-07T03:54:53.623Z",
  "status": "OK",
  "tipo": "MATRIZ",
  "efr": "",
  "motivo_situacao": "",
  "situacao_especial": "",
  "data_situacao_especial": "",
  "capital_social": "200000.00",
  "extra": {},
  "billing": {
    "free": true,
    "database": true
  }
}
"""

def get_infos(cnpjs):
    # for i in cnpjs:
    # i_data = requests.session().get(url+cnpjs)
    i_data = requests.get(url+cnpjs)
    # print i_data.content
    return i_data.content

# data = json.loads(get_infos(cnpj))

for company in list_cnpj:
    print company
    data = json.loads(get_infos(company))


    print data

    data = json.loads(json_example)
    data = json.loads(company)


    if data['status'] != 'ERROR':
    
        cnpj = company
        main_activity = data['atividade_principal'][0]['code']
        company_name = data['nome']
        uf = data['uf']
        neighborhood = data['bairro']
        street = data['logradouro']
        number_address = data['numero']
        zipcode = data['cep']
        city = data['municipio']
        since = data['abertura']
        natureza_juridica =  data['natureza_juridica']
        kind = data['tipo']
        capital = data['capital_social']
        secondary_activities = ''
        situacao = data['situacao']
        data_situacao = data['data_situacao']
    
        #faltam dados de atividades_secundarias . code
        for i in data['atividades_secundarias']:
            secondary_activities += i['code'] + ' | '
        secondary_activities = secondary_activities[:-2]
    
        with open('20180724_csv_cnaes.csv', 'a') as file:
            string = ''
            csv_row = [cnpj,main_activity,secondary_activities,company_name,uf,neighborhood,street,number_address,zipcode,city,since,natureza_juridica,kind,capital,situacao,data_situacao]
            for i in csv_row:
                string += i + ';'
            new_string = string[:-1]
            new_string += '\n'
            file.write(new_string)
            file.close()
    else:
        print company
    time.sleep(25)
```