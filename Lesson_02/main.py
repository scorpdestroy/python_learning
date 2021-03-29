from flask import Flask

app = Flask('app')

@app.route('/author')
def author():
    return '''<html>
<body>

<p>
Возможно пример не будет работать должным образом, если ваш браузер не позволяет вставлять одну текстовую область в другую,
т.к. наш редактор использует текстовую область для ввода исходного кода.
</p>

<textarea rows="4" cols="25">
На уроках HTML вы найдете исчерпывающий материал по языку разметки HTML,
изучив который, вы сможете создавать HTML страницы и сделать свой собственный веб сайт. 
'''

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Внутренняя таблица стилей</title>
<style type="text/css">
body {
    background-color:green;
}
h1{
   color: blue;
   font-family:verdana;
}
p{
   font-size:20px;
   color:red;
   text-align:center;
}
</style>
</head>
  <body> 
    <h1>Заголовок</h1>
    <p>Текст первый</p>
    <p>Текст второй</p>
    <p><a href='/author'>автор</a></p> 
  </body>
</html>'''

app.run(host='127.0.0.1', port=8080)