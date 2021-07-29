# Видеокурс Flask
[Плейлист](https://www.youtube.com/watch?v=6jxveKOdyNg&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn)

## Урок 1. Простейшее wsgi - приложение на flask
[Видео урока](https://www.youtube.com/watch?v=6jxveKOdyNg&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn)

- WSGI (англ. Web Server Gateway Interface) 

### Обработчик страниц
````
@app.route("/index")
@app.route("/")
def index():
    return "index"
````

## Урок 2. Использование шаблонов страниц сайта
[Видео урока](https://www.youtube.com/watch?v=TSsEMFZVr5E&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=2)

- По умолчанию все шаблоны берутся из папки templates
- Используем шаблонизатор Jinja2
- {{ title }} конструкция для приема параметров в шаблоне
````
@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title="Про Flask")
````

- цикл в шаблоне
````
{% for m in menu %}
<li>{{m}}</li>
{% endfor %}
````

- создана страница base.html с базовым шаблоном, остальные страницы наследуем от этой


