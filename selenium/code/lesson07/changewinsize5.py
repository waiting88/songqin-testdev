# coding:utf8
from selenium import webdriver
executable_path = r"d:\tools\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path)
# 别忘了设置
driver.implicitly_wait(10)







driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

fromEle = driver.find_element_by_id('fromStationText')
fromEle.click()
fromEle.clear()
fromEle.send_keys(u'南京南\n')

toEle = driver.find_element_by_id('toStationText')
fromEle.click()
toEle.clear()
toEle.send_keys(u'杭州东\n')

driver.find_element_by_css_selector('#date_range > ul >li:nth-child(2)').click()

driver.find_element_by_css_selector('div.footer  a:nth-child(1)').click()




driver.quit()