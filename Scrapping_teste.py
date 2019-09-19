import os
import time
import re
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
from collections import counter as cnt
from urllib.request import urlopen as uReq

estado_lista = []
site = ( f'https://empresasdobrasil.com/empresas/{estado}/organizacao-do-transporte-de-carga')

def BeautifulSoup(soup) #input do nome da cidade pela bs4
uClient = uReq(site)
page_soup = soup(uClient.read(), "html.parser")
uClient.close()



class newbot:
    def init (self, nome_bot):
        self.driver = webdriver.chrome()
        estado = estado_lista()
    
    def empresasbr(self):
        try:
            self.driver.get(site)
            self.driver.implicitly_wait(10)

            i = 0
            while True:
                cidade = [1]

                self.driver.find_element_by_xpath('/html/body/div[3]/div/ul').click
                self.driver.find_element_by_xpath('')




