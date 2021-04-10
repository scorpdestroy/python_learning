import requests
from bs4 import BeautifulSoup
import os
import shutil

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

    os.mkdir("c://Users/shumi/Desktop/python_learning/Project1/MANY_THINGS/" + str(x))
    
    full_way_1 = "c://Users/shumi/Desktop/python_learning/Project1/MANY_THINGS/" + str(x)

    for item in items:
        print(item.getText())
        print("===")
        f1 = open("output.txt", 'w')
        f1.write(str(item.getText()))
        f1.close()     

    for item_1 in items_1:
        print(item_1.getText())
        print("===")
        f2 = open("input.txt", 'w')
        f2.write(str(item_1.getText()))
        f2.close()

