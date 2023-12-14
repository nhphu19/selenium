import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='D:/WolfSolutions/selenium/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.set_window_size(1200, 800)

driver.get('https://op.calibee.vn/login')

# Case Fail
driver.find_element('id', 'emailInput').send_keys('nhphu1912@gmail.com')
time.sleep(1)
driver.find_element('id', 'passwordInput').send_keys('calibee@123')
time.sleep(1)
driver.find_element('id', 'loginButton').click()
time.sleep(5)

# Case Pass
driver.find_element('id', 'emailInput').send_keys('nhphu19@gmail.com')
time.sleep(1)
driver.find_element('id', 'passwordInput').send_keys('calibee@123')
time.sleep(1)
driver.find_element('id', 'loginButton').click()

input()
driver.quit()
