import requests
from bs4 import BeautifulSoup
import os

directory = "C:/Users/shumi/Desktop/python_learning/python_tutor_htmls/"
files = os.listdir(directory)

for x in files:
    full_way = directory + x
    
    f = open(full_way, 'r', encoding='utf-8')

    print(full_way)

    read = f.read()
    f.close()

    soup = BeautifulSoup(read, "lxml")
    items = soup.find_all('pre', class_='output')
    items_1 = soup.find_all('pre', class_='input')

    for item in items:
        print(item.getText())
        print("===")

    for item_1 in items_1:
        print(item_1.getText())
        print("===")
    break