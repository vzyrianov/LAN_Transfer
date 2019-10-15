from flask import Flask, request
from flask import send_file,request
from flask import render_template
from flask import make_response
from flask import redirect
from flask import jsonify


app = Flask(__name__)
app.config["DEBUG"] = True

password = ""

@app.route('/', methods = ["GET"])
def index():
   return ""
    #return render_template("index.html") 

@app.route('/file', methods = ["GET", "POST"])
def file():
   #filename = request.form['name']
   filename = request.args.get('filename')
   if(filename == 'test.txt'): 
      return send_file(filename)
   else:
      return ""


if __name__ == '__main__':
   password = ""
   app.run(host='0.0.0.0', debug=True)
