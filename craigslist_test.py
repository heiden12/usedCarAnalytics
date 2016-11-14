import requests
from bs4 import BeautifulSoup as bs4

url = 'http://columbus.craigslist.org/search/cto?query=porsche+944'
rsp= requests.get(url)

#print(rsp.text)

html = bs4(rsp.text, 'html.parser')

cars = html.body.find_all('li', attrs={'class': 'result-row'})
#print(len(cars))

car_1 =  cars[0]
#print(car_1.prettify())

price = car_1.findAll(attrs={'class': 'result-price'})[0].text
print(price)
