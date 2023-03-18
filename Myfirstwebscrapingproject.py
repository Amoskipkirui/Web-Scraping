# imports
from bs4 import BeautifulSoup
import requests
import pandas as pd

html_page = requests.get('https://www.marketwatch.com/tools/screener/premarket') # Make a get request to retrieve the page
soup = BeautifulSoup(html_page.text, 'html.parser')

# if we access directly i.e span class_label, there are three more which are the same so we access the before line.
title = soup.find_all('h1', class_ = 'title')

for x in title:
    print (x.text) # prints i.e Premarket Screener

# let's extract our table of interest.
table = soup.find_all('div', class_ = 'element element--table table--fixed screener-table')
 # names of the columns
column_headers = ['Symbol','Company Name', 'Price','Volume', 'change$', 'change%']
#We  then  pass these to a dataframe.
dataframe = pd.DataFrame(columns= column_headers)
symbol = ''
company_name = ''
price = ''
volume = ''
change = ''
change_percent = 0 # initializing change_percent to 0 makes it an interger
 
 # to remove hyperlinks in the rows use the below code;

for tr in soup.select ('a'):
    tr.extract()

i = 1
for tr in table[0].find_all ('tr'):
   i = 0
# loops through all the data in table rows(tr) i.e table data(td)
   for td in tr.find_all('td'):
      i=i+1
      if (i==1):
          symbol = td.text.replace('\n', '')
      if (i==2):
          company_name = td.text.replace('\n', '')
      if (i==3):
          price = td.text.replace('\n', '')
      if (i==4):
          volume = td.text.replace('\n', '')
      if (i==5):
          change = td.text.replace('\n', '')
      if (i==6):
          change_percent = float(td.text.replace('\n', '').replace ('%','') ) 
   if (symbol!= ''):
          dataframe = dataframe.append(
          pd.Series ([
          symbol,
          company_name,
          price,
          volume,
          change,
          change_percent 
          ],
          index= column_headers),
          ignore_index = True)
dataframe.sort_values('change%', axis = 0, ascending = False, inplace = True, na_position = 'last')
print(dataframe)