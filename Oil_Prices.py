#import the library used to query a website
import requests

#specify the url
page = requests.get("https://dolar.wilkinsonpc.com.co/commodities/petroleo-wti.html")

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page.content, 'html.parser')

#Find de values within the html
right_table=soup.find_all('td', class_='tabla_historico-periodos_td')
valores = [pt.get_text() for pt in right_table]

#print(valores)

#import the library used to create a csv
import csv

#Write the values in a csv
with open('Oil_Prices.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([valores])
