import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome() #创建一个实例。就是打开浏览器
driver.maximize_window() #窗口最大化
url = 'http://10.10.10.11/doc/page/login.asp?_1663739312352'
driver.get(url)
time.sleep(2) #延迟3秒，等待加载完成

Name = driver.find_element(by=By.ID, value="username")
Name.send_keys("admin")

PW = driver.find_element(by=By.ID, value="password")
PW.send_keys("Along#011")
PW.send_keys(Keys.ENTER)
#driver.find_element(by=By.XPATH, value="/html/body/div/div/table/tbody/tr/td[2]/div/div[5]/button").click() #用XPATH来等位元素，并点击

driver.find_element(by=By.CSS_SELECTOR, value="#nav > li:nth-child(5) > a").click()

time.sleep(5)

time.sleep(1)
time.sleep(12)
#driver.quit()


