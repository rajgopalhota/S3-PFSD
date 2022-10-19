#import Flask
from flask import *
from pymongo import *

#Create an Instance
app = Flask(__name__)

#Normal Route
# @app.route("/")

#define method
# def sample():
#     return "<h1>WELCOME TO FLASK</h1>"

#dynamic routing
# @app.route("/<name>")
# def sample2(name):
#     return f'Hello {name}'
#

#template rendering
@app.route("/template")
def sample3():
    return render_template('index.html')
#Give the template directeory in address bar to get index.html


#for redirect /route has to be placed
@app.route("/template1/<name>")
def sample5(name):
    return render_template('index1.html',name = name)
@app.route("/route/template2/<role>")
def sample4(role):
    if role == "guest":
        return redirect(url_for('sample5',name = role))
    else:
        return redirect(url_for('sample3'))
#
# #List rendering with for tag
@app.route("/list/rendering")
def sample6():
    lst = ['abc', 'def', 'ghi']
    return render_template('index2.html', name = lst)


#Template inheritance
@app.route("/greeting/abc")
def sample7():
    return render_template('home.html')



#Conditional rendering with if tag
@app.route("/conditional/def/")
def sample8():
    role = 'something'
    return render_template('iftag.html',role = role)




#Flask - Form example
@app.route('/form/studentform')
def sample9():
    return render_template('studentform.html')


#Flask Form handling using flask
@app.route('/form/example', methods=('POST', 'GET'))
def sample10():
    if request.method == 'POST':
        name = request.form.get('stu_name')
        number = request.form.get('stu_no')
        return render_template('studentdetails.html', name=name, number = number)
    else:
        return "Invalid logn"

#Flask Bootstrap
@app.route("/bootstrapexample")
def sample11():
    return render_template('bootstraphome.html')


#Flask CRUD operations(mongo)
client = MongoClient("mongodb://127.0.0.1:27017")
db = client['StudentFlaskDB']
studentdata = db.details
@app.route("/")
def form():
    return render_template('forms.html')

@app.route("/successfull", methods=('POST', 'GET'))
def onsubmit():
    fn = request.form.get('fn')
    ln = request.form.get('ln')
    mb = request.form.get('mb')
    regno = request.form.get('regno')
    a = {"First Name": fn, "Last Name": ln, "Mobile": mb, "Regd No": regno}
    studentdata.insert_one(a)
    return "Successfully submitted"






if __name__ == "__main__":
    app.run()