from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv
import os

options = Options()
# options.headless = True
options.add_argument("--no-sandbox")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors')
index0=[]
index1=[]
index2=[]
index3=[]
index4=[]
csvinput=[]
driver = webdriver.Chrome(options=options, executable_path='/home/tarek/Selenium_Projects/webdrivers/chromedriver')
strings=[]
with open('strings_import_data.csv', 'r') as file:
    reader = csv.reader(file)
    for csvline in reader:
        strings.append(csvline)

for string in strings:
    time.sleep(1)
    driver.get("https://duckduckgo.com/")
    time.sleep(3)
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(string)
    que.send_keys(Keys.RETURN)
    time.sleep(5)
    try:
        titles = driver.find_elements_by_xpath("//div[5]/div/div/h2/a[1]")
        title1 = titles[0].text
        title2 = titles[1].text
    except:
        title1 = 'could not locate'
    print(title1)
    try:
        urls = driver.find_elements_by_xpath("//div[5]/div/div/h2/a[1]")
        url1 = urls[0].get_attribute('href')
        url2 = urls[1].get_attribute('href')
    except:
        url1 = 'could not locate'
    print(url1)
    time.sleep(2)
    index0.append(string)
    index1.append(title1)
    index2.append(url1)
    index3.append(title2)
    index4.append(url2)
    print(f"Completed: {string}")
driver.quit()
data = {'string': index0,
        'title1': index1,
        'url1': index2,
        'title2': index3,
        'url2': index4
        }
df = pd.DataFrame (data, columns = ['string','title1','url1','title2','url2'])
df.to_csv (r'DuckDuckGo_export_data.csv', index = False, header=True)
print (df)

