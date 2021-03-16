from requests_html import HTMLSession
session = HTMLSession()
import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd


col1 = []
col2 = []
response = session.get('https://www.google.com/search?q=selenium')
#l = response.html.links
link = response.html.xpath('//div[@class="g"]//div/div[1]/a/@href')
text = response.html.xpath('//div[@class="g"]//h3')
for i in range(2):
 url = link[i]
 col1.append(url)
 title = text[i].text
 col2.append(title)
 
 print(url)
 print(title)

data= {'title':col2,
'url':col1}
print(data)

df = pd.DataFrame(data)
new_df = df.T

print(df)
print(new_df)
