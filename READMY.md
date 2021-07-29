# Видеокурс Flask
[Плейлист](https://www.youtube.com/watch?v=6jxveKOdyNg&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn)

## Урок 1. Простейшее wsgi - приложение на flask.
[Видео урока](https://www.youtube.com/watch?v=6jxveKOdyNg&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn)

- WSGI (англ. Web Server Gateway Interface) 

### Обработчик страниц (Декораторы)
````
@app.route("/index")
@app.route("/")
def index():
    return "index"
````

## Урок 2. Использование шаблонов страниц сайта.
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

## Урок 3. Контекст приложения и контекст запроса.
[Видео](https://www.youtube.com/watch?v=tP09rxKbNMU&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=3)

- Контекст приложния
    - g
    - current_app
- Контекст запроса
    - request
    - session
    
## Урок 4. Функция url_for и переменные URL-адреса
[Видео](https://www.youtube.com/watch?v=oM39KVYsjRs&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=4)

### Тестовый контекст запроса и url_for
````
with app.test_request_context():
    print( url_for('index'))
````

### Динамические url адреса
````
@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"
````

````
@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"
````

- path
- int
- float