#import Flask
from flask import Flask, render_template, redirect, url_for

#Create an Instance
app = Flask(__name__)

#Normal Route
@app.route("/")

#define method
def sample():
    return "<h1>WELCOME TO FLASK</h1>"

# #dynamic routing
# @app.route("/<name>")
# def sample2(name):
#     return f'Hello {name}'
#
#
# #template rendering
# @app.route("/template")
# def sample3():
#     return render_template('index.html')
# #Give the template directeory in address bar to get index.html
#
#
# #for redirect /route has to be placed
# @app.route("/template1/<name>")
# def sample5(name):
#     return render_template('index1.html',name = name)
# @app.route("/route/template2/<role>")
# def sample4(role):
#     if role == "guest":
#         return redirect(url_for('sample5',name = role))
#     else:
#         return redirect(url_for('sample3'))
#
# #List rendering with for tag
# @app.route("/list/rendering")
# def sample6():
#     lst = ['abc', 'def', 'ghi']
#     return render_template('index2.html', name = lst)
#

#Template inheritance
@app.route("/greeting/abc")
def sample7():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()