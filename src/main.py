from flask import Flask, request
from flask import send_file,request
from flask import render_template
from flask import make_response

from os import listdir
from os.path import isfile, join

app = Flask(__name__)
app.config["DEBUG"] = True

password = ""

@app.route('/', methods = ["GET"])
def index():

   files = [f for f in listdir('.') if isfile(join('.',f))]
   
   return render_template("index.html", files = files) 

@app.route('/file', methods = ["GET", "POST"])
def file():
   #filename = request.form['name']
   filename = request.args.get('filename')
   return send_file(filename)


if __name__ == '__main__':
   password = ""
   app.run(host='0.0.0.0', debug=True)
