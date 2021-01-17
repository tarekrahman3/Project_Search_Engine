from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd
import csv
import os

options = Options()
options.headless = True
options.add_argument("--no-sandbox")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors')

text = []
url = []
rows = []

driver = webdriver.Chrome(options=options, executable_path='/home/tarek/Selenium Projects/Google Search Result First Link/chromedriver')
Strings = []

with open('Strings_import_data.csv', 'r') as file:
    reader = csv.reader(file)
    for csvline in reader:
	    data = csvline
	    csvinput = '\n'.join(data)
	    Strings.append(csvinput)

for string in Strings:
    time.sleep(3)
    driver.get('http://www.google.com')
    time.sleep(4)
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys("site:linkedin.com/company/ ", string)
    time.sleep(4)
    que.send_keys(Keys.RETURN)
    time.sleep(8)
    
    try:
	col__1 = driver.find_element(By.ID, "rso").find_element_by_xpath('.//span[1]').text
    except:
	col__1 = 'N/A'
    col_1 = ['Title:', col__1]
    text.append(col_1)
    
    try:
        col__2 = driver.find_element(By.ID, "rso").find_element_by_xpath('.//a').get_attribute('href')
    except:
	col__1 = 'N/A'
    col_2 = ['Website:', col__2]
    url.append(col_2)
    row = [col_1, col_2]
    rows.append(row)
    time.sleep(4)

for data in rows:
    print(data)

driver.quit()
