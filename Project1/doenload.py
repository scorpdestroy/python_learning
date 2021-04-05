import requests
from bs4 import BeautifulSoup

url = 'https://pythontutor.ru/lessons/inout_and_arithmetic_operations/problems/aplusbplusc/'

response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text, 'lxml')

items = soup.find_all('li', class_='input')
roar = soup.find_all('li', class_='output')
print(items)
print(roar)
f = open('links.txt', 'a', encoding='utf-8')

for item in items:
    href = item.find('a').get('href')
    print(href)
    f.write(href + '\n')
f.close()