#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import importlib
importlib.reload(sys)

import time
import requests
import csv

url = "https://rdap.registro.br/domain/"

domains = ['stz.com.br',
'viasullogistica.com',
'eletronor.com',
'intelbras.com.br',
'bmlog.com.br',
'blueticket.com.br',
'taai.com.br',
'dgranel.com.br',
'baspan.com.br',
'karsten.com.br',
'yes.ind.br',
'latitudelog.com.br',
'intelbras.com.br',
'gmail.com',
'tketransporte.com.br',
'asserttecnologia.com.br',
'eletronor.com',
'intelbras.com.br',
'refnicnil.com.br',
'transpocrgo.com.br',
'gmail.com',
'positivo.com.br',
'intelbras.com.br',
'tsilvio.com.br',
'unimartra.com.br',
]


def get_url(domain):
    session = requests.Session()
    session.get(url)
    r = requests.get(url+domain)
    if r.status_code == 200:
        return r.json()
    else:
        return None

def get_document(json):
    if "entities" in json.keys():
        entities = json["entities"]
        for entity in entities:
            if "publicIds" in entity:
                public_ids = entity["publicIds"]
                for ids in public_ids:
                    if ids["type"] == "cnpj":
                        return ids["identifier"]

def append_to_csv(domain, document, json):
    file = open('leads_evento_agile_CNPJ_leadspedro.csv', 'a')
    csv_row = [domain, document, json]
    string = ''
    for i in csv_row:
        print(i)
        string += str(i) + ';'
    new_string = string[:-1]
    new_string += '\n'
    file.write(new_string)
    file.close()

for domain in domains:
    json = get_url(domain)
    if json is not None:
        append_to_csv(domain, get_document(json), json)
    time.sleep(10)
