from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import time

CNPJ_LIST = [
'60453032000174',
'82762121000135',
'14926356000246',
'02236201000118',
]

def sanitize_cnpj(cnpj):
    return re.sub(r"\D", "", cnpj)  

def get_paragraphs_from_page(cnpj):
    sanitized_cnpj = sanitize_cnpj(cnpj)
    req = requests.get (f'https://cnpj.biz/{sanitized_cnpj}')
    if req.status_code == 200:
        content = req.text
        soup = BeautifulSoup(content, 'html.parser')
        body = soup.find('body')
        if body is not None:
            container = body.find('div', 'container', recursive=False)
            if container is not None:
                hero = container.find('div', 'hero')
                if hero is not None:
                    info_div = hero.find('div', 'row')
                    if info_div is not None:
                        info_col = info_div.find('div', 'c9-2')
                        if info_col is not None:
                            return info_col.find_all('p')
                        else: return []
                    else: return []
                else: return []
            else: return []
        else: return []
    else:
        return []

ATTRIBUTES_WE_WANT = ['CNPJ', 'Nome Fantasia', 'Razão Social', 'Natureza Jurídica', 'Situação']
def extract_name_and_value_from_paragraphs(paragraphs):
    all_attribute_names =  list(map(lambda p: p.find(text=True, recursive=False), paragraphs))
    all_attribute_values = list(map(lambda p: get_value_from_paragraph(p), paragraphs))
    attribute_names = []
    attribute_values = []
    for index in range(len(ATTRIBUTES_WE_WANT)):
        attr_name = ATTRIBUTES_WE_WANT[index]
        attribute_names.append('')
        attribute_values.append('')
        for attr_name_2 in all_attribute_names:
            if attr_name in attr_name_2:
                value_index = all_attribute_names.index(attr_name_2)
                attribute_names[index] = attr_name_2
                attribute_values[index] = all_attribute_values[value_index]
    return attribute_names, attribute_values

def get_value_from_paragraph(p):
    bold_text = p.find('b')
    if bold_text is None:
        return ''
    else:
        return bold_text.get_text()
        

file = open('teste_anvisa_1.csv', 'a')

for cnpj in CNPJ_LIST:
    paragraphs = get_paragraphs_from_page(cnpj)
    attr_names, attr_values = extract_name_and_value_from_paragraphs(paragraphs)
    comma_separated_values = (';').join(attr_values)
    comma_separated_values += '\n'
    file.write(comma_separated_values)
    time.sleep(10)

file.close()

