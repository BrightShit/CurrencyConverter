import os
from bs4 import BeautifulSoup
import requests
import time
def dollar__():
    from__=input("Choose currency that you want to convert from example(USD)\n")
    to__ =input("Choose currency that you want to convert to\n")
    google ='https://www.xe.com/currencyconverter/convert/?Amount=1&From='+from__.upper()+'&To='+to__.upper()
    print(google)
    source = requests.get(google).text
    soup = BeautifulSoup(source,'lxml')
    dollar = soup.find("p",class_="result__BigRate-sc-1bsijpp-1 iGrAod")
    dollar__to__float=dollar.text.split(" ")
    #(Line 3-9) it will help me to get the updated dollar rate 
    new__dollar=dollar__to__float[0]
    new__dollar = str(new__dollar)
    new__dollar = float(new__dollar)
    #(Line 10-13)Converting the text into a float 
    how__many__dollars=float(input("What is the price: \n"))
    try:
        float(how__many__dollars)
    except:
        print("Please choose a number")
    sum__=how__many__dollars * new__dollar
    sum__=round(sum__,2)
    print(sum__)
    while 1:{}
dollar__()
