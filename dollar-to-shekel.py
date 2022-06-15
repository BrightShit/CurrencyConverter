from bs4 import BeautifulSoup
import requests
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
print(dollar__())
