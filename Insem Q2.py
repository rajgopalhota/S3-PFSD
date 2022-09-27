#import Flask
from flask import Flask, render_template

#Create Reference
app = Flask(__name__)

#dynamic routing
@app.route("/<name>")
def raja(name):
    return f'Hello {name}'

#Main method

if __name__ == "__main__":
    app.run()