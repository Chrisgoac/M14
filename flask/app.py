from flask import Flask
from flask import request

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return {"hello":"Hello World :)", "goodbye":"Goodbye World :("}

@app.route("/construction")
@app.route("/aboutus")
def construction():
    return {"message":"Under construction"}


@app.route("/employee/<name>/")
def show_profile(name):
   return "Employee Name: " + name + "\n"


@app.route("/movies/<genre>/<lang>")
def show_movies(genre, lang):
   return "Movie genre, lang: " + genre + lang + "\n"


@app.route("/movie/<int:id>")
def show_movie_id(id):
   return "Movie ID + 1: " + str(id + 1)

# Exercise 1:

@app.route("/about")
def render_about():
	return "Information about this page"

# Exercise 2:

@app.route("/videos/<name>")
@app.route('/', methods=['POST', 'GET'])

#Exercise 3:

@app.route("/ref")
@app.route("/link")
def connect():
    return "connect.html"


# REQUESTS:

@app.route('/user/<int:id>', methods=['POST', 'GET'])
def user(id):
    if request.method == "GET":
        return "GET: User info"
    elif request.method == "POST":
        if "token" in request.form:
            token = request.form.get("token")
            if token == "abc":
                return "User has been authenticated"
            return "Failed token authentication"
        return "You must pass a token"
       
# PARAMETROS DE CONSULTA

@app.route('/users')
def users():
    query_params = request.args
    city = query_params.get("city")
    age = query_params.get("age")
    
    result = get_users(city, age)
    return str(result)

def get_users(city, age):
    if city == "Barcelona":
        return ["Adolf", "Hitler"]
    else:
        return ["Pepe", "Peparro"]
    


if __name__ == "__main__":
    app.run()