from bs4 import BeautifulSoup

f = open('resp.html', 'r', encoding='utf-8')

text = f.read()
f.close()

soup = BeautifulSoup(text, 'lxml')

items = soup.find_all('li', class_='problem-available')
#print(items)
f = open('links.txt', 'a', encoding='utf-8')
for item in items:

    href = item.find('a').get('href')
    print(href)
    f.write(href + '\n')
f.close()