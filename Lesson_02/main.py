from flask import Flask

app = Flask('app')

@app.route('/first_part')
def first_part():
    return '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Внутренняя таблица стилей</title>
<style type="text/css">
body {
    background-color:Tomato;
}
h1{
   color: blue;
   font-family:verdana;
}
p{
   font-size:70px;
   color:blue;
   text-align:center;
}
</style>
</head>
  <body> 
    <p>Был</p>
    <p><a href='/'>оглавление</a></p> 
  </body>
</html>
'''

@app.route('/second_part')
def second_part():
    return '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Внутренняя таблица стилей</title>
<style type="text/css">
body {
    background-color:Tomato;
}
h1{
   color: blue;
   font-family:verdana;
}
p{
   font-size:70px;
   color:LightBlue;
   text-align:center;
}
</style>
</head>
  <body> 
    <p>Жил</p>
    <p><a href='/'>оглавление</a></p> 
  </body>
</html>

'''

@app.route('/third_part')
def third_part():
    return '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Внутренняя таблица стилей</title>
<style type="text/css">
body {
    background-color:Tomato;
}
h1{
   color: blue;
   font-family:verdana;
}
p{
   font-size:70px;
   color:LightBlue;
   text-align:center;
}
</style>
</head>
  <body> 
    <p>Всплыл</p>
    <p><a href='/'>оглавление</a></p> 
  </body>
</html>

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
    background-color:Tomato;
}
h1{
   color: blue;
   font-family:verdana;
}
p{
   font-size:20px;
   color:LightBlue;
   text-align:center;
}
</style>
</head>
  <body> 
    <h1>Оглавление</h1>
    <p><a href='/first_part'>Первая глава</a></p>
    <p><a href='/second_part'>Вторая глава</a></p>
    <p><a href='/third_part'>Третья глава</a></p> 
  </body>
</html>'''

app.run(host='127.0.0.1', port=8080)