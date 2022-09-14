from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import re
import os

class turboself():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.PhantomJS("drivers\phantomjs.exe")

    def purge(self, string : str):
        return string.replace("\n", "").replace(" ","")

    def delete_last_line(self):
        "Use this function to delete the last line in the STDOUT"
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
    
    def connect_(self):
        self.browser.get("https://espacenumerique.turbo-self.com/Connexion.aspx")
        self.browser.find_element_by_id("ctl00_cntForm_txtLogin").send_keys(self.username)
        self.browser.find_element_by_id("ctl00_cntForm_txtMotDePasse").send_keys(self.password)
        self.browser.find_element_by_id("ctl00_cntForm_chkRememberMe").click()
        self.browser.find_element_by_id("ctl00_cntForm_btnConnexion").click()

    def CrediterCompte(self) -> tuple:
        self.browser.get("https://espacenumerique.turbo-self.com/CrediterCompte.aspx")
        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        price = float(self.purge(soup.find_all(class_="prix")[0].string)[:-1].replace(",",'.'))
        left = int(re.findall('[0-9]+', soup.find_all(class_="small")[0].string)[0])
        for i in soup.find_all("strong"):
            if "€" in i.string:
                each = i.string
                break
        dinner = float(self.purge(each)[:-1].replace(",",'.'))
        return (price, dinner, left)