from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('headless') #nao renderiza o browser

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://transferwise.com/gb/currency-converter/brl-to-usd-rate?amount=1000')

result = driver.find_element_by_xpath('//*[@id="cc-amount-to"]')
print(result.get_attribute('value'))