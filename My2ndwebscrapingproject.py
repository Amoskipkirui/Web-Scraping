import requests
from bs4 import BeautifulSoup
import pandas as pd

html_page = requests.get('http://books.toscrape.com/') 
soup = BeautifulSoup(html_page.content, 'html.parser')
print(soup)

title = soup.find_all('div', class_ = 'alert alert-warning')
for x in title :
    print(x.text)

table = title.nextSibling.nextSibling
print(table)