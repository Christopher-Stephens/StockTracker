#imports
import requests
from bs4 import BeautifulSoup

#connecting to site and setting up for data extraction
URL='https://finance.yahoo.com/quote/GE/history?p=GE'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
page = requests.get(URL, headers=headers)
print(f"page.ok : {page.ok} , page.status_code : {page.status_code}")
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find('tbody')
data =[tr_element for tr_element in results]

#Getting data and opening and closing data
for str in data:
    date_Element = str.find('td', class_ = 'Ta(start)').text
    number_Data = str.find_all('td', class_ = 'Py(10px) Pstart(10px)')
    if number_Data != []:
        open_Element = number_Data[0].text
        close_Element = number_Data[3].text
    
    print(f"Date: {date_Element}, Open: {open_Element} and Close: {close_Element}")
          