#import Flask
from flask import Flask

#Create an Instance
app = Flask(__name__)

#Normal Route
@app.route("/")

#define method
def sample():
    return "<h1>WELCOME TO FLASK</h1>"


if __name__ == "__main__":
    app.run()