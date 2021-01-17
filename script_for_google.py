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

csvinput=[]
driver = webdriver.Chrome(options=options, executable_path='/home/practice_environment/chromedriver')
strings=[]
with open('strings_import_data.csv', 'r') as file:
    reader = csv.reader(file)
    for csvline in reader:
        strings.append(csvline)
for string in strings:
    index0.append(string)
    time.sleep(1)
    driver.get("https://www.google.com")
    time.sleep(3)
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys("site:linkedin.com/company/ ", string)
    que.send_keys(Keys.RETURN)
    time.sleep(5)
    try:
        titles = driver.find_elements_by_xpath("//div[@class='g']")
        for each_title in titles:
            title = each_title.find_element_by_xpath(".//div[@class='yuRUbf']/a/h3").text
    except:
        title = 'could not locate'
    index1.append(title)
    try:
        urls = driver.find_elements_by_xpath("//div[@class='g']")
        for each_url in urls:
            url = each_url.find_element_by_xpath(".//div[@class='yuRUbf']/a").get_attribute('href')
    except:
        url = 'could not locate'
    index2.append(url)
    time.sleep(2)
    print(f"Completed: {string}")
driver.quit()
data = {'string':  index0,
        'title':  index1,
        'url': index2
        }
df = pd.DataFrame (data, columns = ['string','title','url'])
df.to_csv (r'GoogleSearch_export_data.csv', index = False, header=True)
print (df)
