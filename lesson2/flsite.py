# https://www.youtube.com/watch?v=TSsEMFZVr5E&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=2
from flask import Flask, render_template

app = Flask(__name__)


menu = ["Установка", "Первое приложение", "Обратная связь"]


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title="О сайте", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
