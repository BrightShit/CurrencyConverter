import os
from bs4 import BeautifulSoup
import requests
import time
def the__whole_thing():
    def dollar__():
        google ='https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=ILS'
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
        print("This is:",sum__,"Israeli New Shekels")
        #(Line 14-22) Converting dollar to shekel
    #Convert shekel to dollar

    def shekel__To__Dollar():
        google ='https://www.xe.com/currencyconverter/convert/?Amount=1&From=ILS&To=USD'
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
        sum__=float(new__dollar)*float(how__many__dollars)  
        sum__=round(sum__,2)
        print("This is:",sum__,"Israeli New Shekels")

    #Shekel to euro

    def shekel__To_EUR():
        google ='https://www.xe.com/currencyconverter/convert/?Amount=1&From=ILS&To=EUR'
        source = requests.get(google).text
        soup = BeautifulSoup(source,'lxml')
        Euro = soup.find("p",class_="result__BigRate-sc-1bsijpp-1 iGrAod")
        Euro__to__float=Euro.text.split(" ")
        #(Line 3-9) it will help me to get the updated dollar rate 
        new__dollar=Euro__to__float[0]
        new__dollar = str(new__dollar)
        new__dollar = float(new__dollar)
        #(Line 10-13)Converting the text into a float 
        how__many__Euro=float(input("What is the price: \n"))

        try:
            float(how__many__Euro)
        except:
            print("Please choose a number")
        sum__=float(new__dollar)*float(how__many__Euro)  
        sum__=round(sum__,2)
        print("This is:",sum__,"Israeli New Shekels")


    def EUR_To_Shekel():
        google ='https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=ILS'
        source = requests.get(google).text
        soup = BeautifulSoup(source,'lxml')
        Euro = soup.find("p",class_="result__BigRate-sc-1bsijpp-1 iGrAod")
        Euro__to__float=Euro.text.split(" ")
        #(Line 3-9) it will help me to get the updated dollar rate 
        new__dollar=Euro__to__float[0]
        new__dollar = str(new__dollar)
        new__dollar = float(new__dollar)
        #(Line 10-13)Converting the text into a float 
        how__many__Euro=float(input("What is the price: \n"))
        try:
            float(how__many__Euro)
        except:
            print("Please choose a number")
        sum__=float(how__many__Euro) * float(new__dollar)
        sum__=round(sum__,2)
        print("This is:",sum__,"Israeli New Shekels")
    def dollar_rate():
        google ='https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=ILS'
        source = requests.get(google).text
        soup = BeautifulSoup(source,'lxml')
        Euro = soup.find("p",class_="result__BigRate-sc-1bsijpp-1 iGrAod")
        Euro__to__float=Euro.text.split(" ")
        #(Line 3-9) it will help me to get the updated dollar rate 
        new__dollar=Euro__to__float[0]
        new__dollar = str(new__dollar)
        new__dollar = float(new__dollar)
        rate = round(new__dollar,2)
        print("Dollar rate is:",rate)

    





    inta= input("Enter an Option:\n 1) DOLLAR to shekel\n 2) SHEKEL to Dollar\n 3) EUR to shekel\n 4) Shekel to Euro \n 5) Check the DOLLAR rate \n ")
    if inta == "1":
        dollar__()
    elif inta == "2":
        shekel__To__Dollar()

    elif inta == "3":
        EUR_To_Shekel()

    elif inta == "4":
        shekel__To_EUR()
    
    elif inta == "5":
        dollar_rate()


    else:
        os.system("cls")
        print("Please choose a valid option")
        time.sleep(0.7)
        the__whole_thing()

the__whole_thing()
