from flask import Flask, render_template,request



app = Flask(__name__)

"""@app.route('/')
def main():
    return render_template('iris.html')

@app.route('/square',methods=["POST"])
def square():
    if request.method == "POST":
       
        return (request.form['Number'])
"""

import hashlib



@app.route("/")
def index():
    return render_template("iris.html")

@app.route("/square", methods=["POST"])
def validate_user():
    number = request.form.get('number')
    try:
        number = int(number)  
        square = number ** 2  
        return str(square)    
    except ValueError:
        return "Invalid input! Please provide a valid integer."




if (__name__) == ('__main__'):
    app.run(debug = True)
