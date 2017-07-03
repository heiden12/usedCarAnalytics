import requests
from bs4 import BeautifulSoup as bs4

#Allow user to enter vehicle to search for
print("What vehcile would you like to search for?(make+model)")
search = input()

url = 'http://columbus.craigslist.org/search/cto?query=' + search
rsp= requests.get(url)
html = bs4(rsp.text, 'html.parser')
cars = html.body.find_all('li', attrs={'class': 'result-row'})
carsAttrib = html.body.find_all('li', attrs={'class': 'attrgroup'})

#Print the number of results found
print(len(cars), " Vehicles found")

print(carsAttrib.prettify())
#print(cars[0].prettify())

#Return the price of each vehicle returned by search criteria
for x in range(0,len(cars)):
    price = cars[x].findAll(attrs={'class': 'result-price'})[0].text
    print(price)
