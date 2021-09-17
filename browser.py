import os
import shutil
from datetime import time
from time import sleep

import selenium
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.headless = False
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Solex\Desktop\mypthonscripts\ЛКС мирэа\chromedriver.exe',options=options)
    def get_login(self):
        self.driver.get(url = 'https://login.mirea.ru/login/?next=/oauth2/v1/authorize/%3Fresponse_type%3Dcode%26client_id%3DdnOh7sdtPxfyxzbxcMRLksWlCCE3WsgTfRY6AWKh%26redirect_uri%3Dhttps%253A%252F%252Fonline-edu.mirea.ru%252Flogin%252F%26scope%3Dbasic%2Bstudent')
        login_box = self.driver.find_element_by_id('id_login').send_keys(mir_login)
        login_pas = self.driver.find_element_by_id('id_password').send_keys(mir_pas)
        self.driver.find_element_by_id('id_password').send_keys(Keys.ENTER)
        # sleep(3)
        # self.driver.close()
        # self.driver.quit()
        #cookies
    def enter_to_subject(self,need_subject:str):
        try:
            subjects = self.driver.find_elements_by_css_selector('.column.c1')
            #sub = self.driver.find_element_by_partial_link_text('алгоритмы').click()
            sub = None
            mysubjects1 = []
            mysubjects = []
            need_subject = need_subject.lower()
            for subject in subjects:
                mysubjects.append(str(subject.text).lower())
                mysubjects1.append(str(subject.text))
            a = -1
            b = 0
            for subject in mysubjects:
                a = a + 1
                if need_subject in subject:
                    b = a
                    sub = mysubjects1[b]
            print(sub)
            self.driver.find_element_by_partial_link_text(sub).click()
        except Exception as ex:
            print(ex)
    def download_raspisanie(self):
        self.driver.get('https://www.mirea.ru/schedule/')
        sleep(1)
        self.driver.find_element_by_partial_link_text('Институт информационных технологий').click()
        self.driver.find_element_by_partial_link_text('2 курс').click()
        sleep(3)
        if os.path.exists(r'C:\Users\Solex\Desktop\mypthonscripts\ЛКС мирэа\ИИТ_2 курс_21-22_осень.xlsx'):
            os.remove(r'C:\Users\Solex\Desktop\mypthonscripts\ЛКС мирэа\ИИТ_2 курс_21-22_осень.xlsx')
        destination = r'C:\Users\Solex\Desktop\mypthonscripts\ЛКС мирэа'
        source = r'D:\Downloads\ИИТ_2 курс_21-22_осень.xlsx'
        dest = shutil.move(source, destination)
    def close_driver(self,timing:float):
        sleep(timing)
        self.driver.quit()
        self.driver.close()