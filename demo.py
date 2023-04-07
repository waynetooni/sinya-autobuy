from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
from win10toast import ToastNotifier
 
 
# options = Options()
# options.add_argument("--disable-notifications")
 


chrome = webdriver.Chrome()
chrome.get("https://www.sinya.com.tw/member/login/")
chrome.find_element_by_xpath('//*[@id="account"]').send_keys('account')
chrome.find_element_by_xpath('//*[@id="pass"]').send_keys('password')
time.sleep(30)
while True :
    chrome.get("https://www.sinya.com.tw/diy")

    while True:
        try:
            chrome.find_element_by_xpath('//*[@id="header"]/div/div/div[2]/div[2]/div[1]/input').send_keys("3090") # 顯示卡型號
            # chrome.find_element_by_xpath('//*[@id="header"]/div/div/div[2]/div[2]/div[1]/input').send_keys("3080")

            chrome.find_element_by_xpath('//*[@id="header"]/div/div/div[2]/div[2]/div[1]/button').click()
            break
        except:
            pass
    while True :
        time.sleep(1)
        try:
            # chrome.find_element_by_css_selector('div[rel="/upload/prod/s153992.jpg"]').click()
            
            chrome.find_element_by_xpath('//*[@id="app"]/div[3]/div[2]/div/div[3]/div[2]/div[9]/div[1]/div/span').click()
            # chrome.find_element_by_xpath('//*[@id="app"]/div[3]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/span').click()
            break
        except:
            pass
    time.sleep(1)
    
    try:
        chrome.find_element_by_xpath('/html/body/div[10]/div[7]/div/button').click()
    except:
        time.sleep(.500)
        chrome.find_element_by_xpath('/html/body/div[5]/footer/div/div[2]/button[3]').click() # 點擊結帳
        time.sleep(.500)
        try:
            chrome.find_element_by_xpath('//*[@id="collapseOne"]/div/div[2]/div/div/button').click() # 點擊下一步
            time.sleep(.500)
            chrome.find_element_by_xpath('//*[@id="shipment_box"]/div[2]/input').click() # 點擊統一編號
            time.sleep(.500)
            chrome.find_element_by_xpath('//*[@id="shipment_box"]/div[3]/div[1]/input').send_keys("統一編號") # 輸入統一編號
            chrome.find_element_by_xpath('//*[@id="shipment_box"]/div[3]/div[2]/input').send_keys("輸入抬頭") # 輸入抬頭
            time.sleep(.500)
            chrome.find_element_by_xpath('//*[@id="shipment_box"]/div[7]/input').click()  # 選擇店家名稱
            time.sleep(.500)
            chrome.find_element_by_xpath('//*[@id="shipment_box"]/div[8]/div[1]/select/option[4]').click()  # 確認店家名稱
            time.sleep(.500)
        except:
            continue
        
        chrome.find_element_by_xpath('//*[@id="shipment_box"]/div[8]/div[3]/input').send_keys("name")         #姓名
        chrome.find_element_by_xpath('//*[@id="shipment_box"]/div[8]/div[4]/input').send_keys("phone number")     # 手機
        time.sleep(.500)

        chrome.find_element_by_xpath('//*[@id="city"]/option[8]').click() # 確認縣市
        time.sleep(.500)

        chrome.find_element_by_xpath('//*[@id="local"]/option[2]').click()# 確認行政區
        time.sleep(.500)
        
        chrome.find_element_by_xpath('//*[@id="shipment_box"]/div[8]/div[8]/input').send_keys("address") # 地址
        
        time.sleep(.500)
        chrome.find_element_by_xpath('//*[@id="collapseTwo"]/div/div[2]/div/button').click()
        time.sleep(.500)
        chrome.find_element_by_xpath('//*[@id="collapseFour"]/div/div[2]/div/button').click()
        time.sleep(.500)
        ToastNotifier().show_toast(u'緊急',u'搶到貨了!!!')
        time.sleep()
        

    time.sleep(random.randint(5, 10))