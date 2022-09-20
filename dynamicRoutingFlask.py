#import Flask
from flask import Flask, render_template

#Create an Instance
app = Flask(__name__)

#Normal Route
@app.route("/")

#define method
def sample():
    return "<h1>WELCOME TO FLASK</h1>"

#dynamic routing
@app.route("/<name>")
def sample2(name):
    return f'Hello {name}'


#template rendering
@app.route("/template")
def sample3():
    return render_template('index.html')
#Give the template directeory in address bar to get index.html

if __name__ == "__main__":
    app.run()