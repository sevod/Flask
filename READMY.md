# Видеокурс Flask

## Урок 1. Простейшее wsgi - приложение на flask
https://www.youtube.com/watch?v=6jxveKOdyNg&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn

WSGI (англ. Web Server Gateway Interface) 

###обработчик страниц
````
@app.route("/index")
@app.route("/")
def index():
    return "index"
````
