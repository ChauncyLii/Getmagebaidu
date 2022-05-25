from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
import time
from DownloadFile import Download


# 隐藏WebDriver提示条和自动化扩展信息来跳过验证
option=ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_experimental_option('useAutomationExtension',False)

driver = webdriver.Chrome(service=Service(r'D:\software_testing\ToolWebdriver\chromedriver.exe'),options=option)
driver.get("https://image.baidu.com/")
elem = driver.find_element(By.NAME,"word").send_keys('IU\n')
time.sleep(1)
driver.execute_script("var q = document.documentElement.scrollTop=700") # 模拟鼠标滚轮
# main_img img-hover
time.sleep(1)
img = driver.find_elements(By.XPATH,'//a/img[@class="main_img img-hover"]')
print('获取到的图片链接有 {} 张'.format(len(img)))
down = Download()
i = 0
while i<len(img):
    pic_name = '{}.jpg'.format(i)
    down.download_img(pic_name,img[i].get_attribute('src'))
    i=i+1

driver.close()