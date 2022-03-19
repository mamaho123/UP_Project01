import os
import sys
from tkinter import E
import pandas as pd
import time
import pyautogui
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)


def getTB():
    try:
        filePath = os.listdir(os.path.join(application_path, 'Data'))[-1]
        filePath = os.path.join(application_path, 'Data', filePath)
        if os.path.splitext(os.path.basename(filePath))[0].split('_')[-1] == 'inputData':
            tb1 = pd.read_csv(filePath, dtype='str')
            return tb1
    except Exception as e:
        print('File not found!')
        pyautogui.alert(text="File not found!\n" + str(e),
                        title='ERROR', button='OK')
        sys.exit()


def main():
    tb = getTB()

    _setting = os.path.join(application_path, "setting.json")
    jSetting = json.load(open(_setting))
    d1 = jSetting['parameter']['delay']['d1']
    d2 = jSetting['parameter']['delay']['d2']
    screen_x = jSetting['parameter']['screen']['x']
    screen_y = jSetting['parameter']['screen']['y']

    useDriver = 'chrome'
    for i in jSetting['parameter']['driver']:
        if jSetting['parameter']['driver'][i] == 1:
            useDriver = i

    try:
        if useDriver == 'chrome':
            # Setting the Chrome option
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_argument(f"window-size={screen_x},{screen_y}")
            driver = webdriver.Chrome(chrome_options=options, executable_path=os.path.join(
                application_path, 'Driver', 'chromedriver.exe'))
        elif useDriver == 'ie':
            options = webdriver.IeOptions()
            options.add_additional_option("detach", True)
            options.add_argument(f"window-size={screen_x},{screen_y}")
            driver = webdriver.Ie(options=options, executable_path=os.path.join(
                application_path, 'Driver', 'IEDriverServer.exe'))

        driver.get(r'http://192.168.1.37:3000/')
        errMsg = ''
        cnt = 0
        for i, tr in tb.iterrows():
            try:
                login_Register_Link_xPath = '/html/body/div/div/div/div[2]/div/p[3]/a'
                login_Register_Link = driver.find_element(
                    By.XPATH, login_Register_Link_xPath)
                login_Register_Link.click()

                tbx_username = driver.find_element(
                    By.XPATH, '/html/body/div/div/div/div/div[2]/div/form/div[1]/input')
                tbx_empNumber = driver.find_element(
                    By.XPATH, '/html/body/div/div/div/div/div[2]/div/form/div[2]/input')
                tbx_email = driver.find_element(
                    By.XPATH, '/html/body/div/div/div/div/div[2]/div/form/div[3]/input')
                tbx_password = driver.find_element(
                    By.XPATH, '/html/body/div/div/div/div/div[2]/div/form/div[4]/input')
                tbx_rePassword = driver.find_element(
                    By.XPATH, '/html/body/div/div/div/div/div[2]/div/form/div[5]/input')
                chk_agree = driver.find_element(
                    By.XPATH, '/html/body/div/div/div/div/div[2]/div/form/div[6]/div[1]/div/label')
                btn_submit = driver.find_element(
                    By.XPATH, '/html/body/div/div/div/div/div[2]/div/form/div[6]/div[2]/button')
                # btn_regisOK = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[6]/button[1]')

                tbx_username.send_keys(tr.username)
                tbx_empNumber.send_keys(tr["empNumber"])
                tbx_email.send_keys(tr.email)
                tbx_password.send_keys(tr.password)
                tbx_rePassword.send_keys(tr.password)
                chk_agree.click()
                btn_submit.click()

                time.sleep(d1)

                try:
                    resPass = True if driver.find_element(
                    By.XPATH, '/html/body/div[2]/div/h2').text == 'Register success!' else False
                    driver.find_element(
                        By.XPATH, '/html/body/div[2]/div/div[6]/button[1]').click()

                    if not resPass:
                        driver.find_element(
                            By.XPATH, '/html/body/div/div/div/div/div[1]/a').click()
                        print(f'Register Fail : {tr.empNumber}')
                        errMsg += f'Register Fail at : {i} - {tr.empNumber}\n'
                    else:
                        cnt += 1
                except Exception as e:
                    driver.find_element(
                            By.XPATH, '/html/body/div/div/div/div/div[1]/a').click()
                    print(f'Register Fail : {tr.empNumber}')
                    errMsg += f'Register Fail at : {i} - {tr.empNumber} >input error\n'
                

                # print(driver.current_url)
            except:
                print(f'Input Error at : {i} - {tr.empNumber}')
                errMsg += f'Register Fail : {tr.empNumber}\n'

        pyautogui.alert(
            text=f'Process Complete!\n{cnt} item(s) has been register. (of {tb.shape[0]})', title='Process complete',
            button='OK')
        if errMsg != '':
            pyautogui.alert(
                text=f'{tb.shape[0]-cnt} item(s) error.\n--------------------\n' + errMsg, title='ERROR', button='OK')

    except Exception as e:
        pyautogui.alert(text="Something wrong!\n" +
                        str(e), title='ERROR', button='OK')


main()
