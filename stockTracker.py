#imports
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])


def getStockTracking():
     #getting the user desired stock
    stockTicker = " "
    closingArray= []
    dateArr = []
    if request.method == 'POST':
        stockTicker = request.form['ticker']
        results,closingArray,dateArr = stockTracking(stockTicker) 
    else:
         results=[]   
    return render_template("index.html", results=results, ticker=stockTicker, closingArray=closingArray, dateArr=dateArr)

def stockTracking(st):
    closingArray = []
    dateArray =[]
    #connecting to site and setting up for data extraction
    URL='https://finance.yahoo.com/quote/'+st+'/history?p=GE'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    if page.ok != True:
         return ["There was an error connecting. Try Again"]
    print(f"page.ok : {page.ok} , page.status_code : {page.status_code}")
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find('tbody')
    data =[tr_element for tr_element in results]
    results=[]
    #Getting data and opening and closing data
    for str in data:
        date_Element = str.find('td', class_ = 'Ta(start)').text
        number_Data = str.find_all('td', class_ = 'Py(10px) Pstart(10px)')
        if number_Data != []:
            open_Element = number_Data[0].text
            close_Element = number_Data[3].text
        #Formating results with error handiling
        try:
            results += [f"Date: {date_Element}, Open: {open_Element} and Close: {close_Element}"]
            closingArray += close_Element
            dateArray += [date_Element]
        except:
             return ["There was an error with the stock ticker. Make sure you put in a correct ticker. Try Again"]
    #Taking out duplicates
    temp = results[0]
    for dup in results:
            if temp == dup:
                if dup != results[0]:
                    results.remove(dup)
            temp = dup

    return results,closingArray,dateArray
  #gettng the percentage of change in the month and adding it to an array      
def monthlyPercentage(open,closing):
    percentages = []
    sum =0.0
    if float(open)>float(closing):
          percentages += -1.0 * float(open/closing)
    elif float(open)<float(closing):
          percentages += float(open/closing)
    for percent in percentages:
          sum += percent
    return sum
#Getting the monthly and overall percentage over the datas time period
def overallPercent(open, closing, date):
    percentArr =[]
    overallP =0
    monthlyP=[]
    index =0
    for day in date:
        dateNum = str(day[4])+str(day[5]) 
        match dateNum:
            case "01":
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 02:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 03:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 04:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 05:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 06:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 07:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 08:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 09:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 10:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 11:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 12:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 13:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 14:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 15:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 16:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 17:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 18:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 19:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 20:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 21:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 22:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 23:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 24:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 25:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 26:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 27:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 28:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 29:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
            case 30:
                monthlyP=monthlyPercentage(open[index],closing[index])
                overallP+=monthlyP
        index+=1               
    return percentArr
    