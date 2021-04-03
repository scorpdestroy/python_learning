import requests

f = open('links.txt', 'r', encoding='utf-8')

link = 'https://pythontutor.ru'

for x in f:
    f = open(x.split('/')[-2] + '.html', 'w', encoding='utf-8')
    final_link = (link + x)
    response = requests.get(final_link)
    f.write(response.text)
    f.close()
f.close()        