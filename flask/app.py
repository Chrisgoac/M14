from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')


@app.route('/publicacions')
def publicacions():
    return render_template('publicacions.html')

@app.route('/novetats')
def novetats():
    return render_template('novetats.html')

@app.route('/subscripcio')
def subscripcio():
    return render_template('subscripcio.html')

if __name__ == "__main__":
    app.run()