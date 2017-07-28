# coding:utf8
from selenium import webdriver
executable_path = r"d:\tools\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path)
# 别忘了设置
driver.implicitly_wait(10)

# 抓取排行榜信息
def getInfo():
    driver.get('http://music.163.com')


    driver.find_element_by_css_selector('#discover-module > div.g-mn1 > div > div > div.n-bill > div.v-hd2 > a').click()








getInfo()

driver.quit()