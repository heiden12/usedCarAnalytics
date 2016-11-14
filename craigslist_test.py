import requests
from bs4 import BeautifulSoup as bs4

print("What vehcile would you like to search for?(make+model)")
search = input()

#url = 'http://columbus.craigslist.org/search/cto?query=porsche+944'
url = 'http://columbus.craigslist.org/search/cto?query=' + search
rsp= requests.get(url)

#print(rsp.text)

html = bs4(rsp.text, 'html.parser')

cars = html.body.find_all('li', attrs={'class': 'result-row'})
print(len(cars), " Vehicles found")

car_1 =  cars[0]
#print(car_1.prettify())

#price = car_1.findAll(attrs={'class': 'result-price'})[0].text
#print(price)

for x in range(0,len(cars)):
    price = cars[x].findAll(attrs={'class': 'result-price'})[0].text
    print(price)
