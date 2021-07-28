from flask import Flask
app = Flask(__name__)


# Create a root route ("/") that responds with "Hello World!"
@app.route('/')
def hello_world():
    return 'Hello World!'


# Create a route that responds with "Dojo!"
@app.route('/dojo')
def Dojo():
    print("Coding Dojo!")
    return 'Dojo!'


# Create a route that responds with "Hi" and whatever name is in the URL after /say/
@app.route('/hi/<string:name>')
def hello(name):
    print(name)
    return "Hi " + name


# Create a route that responds with the given word repeated as many times as specified in the URL
@app.route('/<string:username>/<int:id>')
def show_user_profile(username, id):
    print(username)
    print(f"username: {username}\n" * id)
    return f"username: {username}\n" * id


if __name__=="__main__":
    app.run(debug=True)
