from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.instagram.com/')

sleep(5)

input_username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
input_password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
btn_login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')

input_username.send_keys('jamessonjr@gmail.com')
input_password.send_keys('@961167@')
btn_login.click()

sleep(5)

btn_dont_notify = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
btn_dont_notify.click()



