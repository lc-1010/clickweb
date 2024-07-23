import json
import os
import re
import time
import pdb
import pprint
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from excel_reader import read_keywords_from_excel  # 引入模块

class top5w:
    def __init__(self, url, chrome_path=None, driver=None,excel_file=None,sheet=None, col_name = None):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--enable-logging")
        chrome_options.add_argument("--v=1")
        if chrome_path:
            chrome_options.binary_location = chrome_path
        
        self.dirver = webdriver.Chrome(executable_path=driver, options=chrome_options)

        self.seesion_url = url
        self.dirver.set_page_load_timeout(40)
        if sheet:
            self.sheet = sheet
        else:
            self.sheet = "Sheet1"
        self.col_name = col_name
    
    @property    
    def df(self):
        self.df = read_keywords_from_excel(self.excel_file,self.sheet )
        return self.df 
    
    # 循环处理每个地址
    def loop_click(self):
        for idx, row in self.df.iloc[:].iterrows():
            keyword = row[self.columen_name]
            if keyword == "":
                continue
            print(keyword)
            

if __name__ == "__main__":
    excel_path = '60.xlsx'
    sheet_name = ""
