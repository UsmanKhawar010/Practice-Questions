from flask import Flask, render_template,request
import hashlib

app = Flask(__name__)




@app.route("/")
def index():
    return render_template("task3_evluation.html")

@app.route("/square", methods=["POST"])
def validate_user():
    number = request.form.get('number')
    try:
        number = int(number)  
        
        return "\n \n".join([str(number * i) for i in range(1, 11)])
    
    except ValueError:
        return "Invalid input! Please provide a valid integer."



if (__name__) == ('__main__'):
    app.run(debug=True)