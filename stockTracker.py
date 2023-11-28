
import requests
from bs4 import BeautifulSoup


URL='https://finance.yahoo.com/quote/GE/history?p=GE'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
page = requests.get(URL, headers=headers)
print("page.ok : {} , page.status_code : {}".format(page.ok , page.status_code))
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find('tbody')
data =[tr_element for tr_element in results]

for str in data:
    dateElement = str.find('td', class_ = 'Ta(start)')
    openElement = str.find('td', class_ = 'Py(10px) Pstart(10px)')
    if(openElement != None):
        print(openElement.text)
#print(data)

