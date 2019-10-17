from flask import Flask, request
from flask import send_file,request
from flask import render_template
from flask import make_response,redirect
from os import listdir
from os.path import isfile, join

import random
import string
import socket

app = Flask(__name__)
app.config["DEBUG"] = True

password = ""

def get_local_ip():
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect(("8.8.8.8", 80))
   result = s.getsockname()
   s.close()
   return result[0]

def generate_random_password():
   letters = string.ascii_letters
   return ''.join(random.choice(letters) for i in range(5))

def logged_in(input_pass):
   return input_pass != None and input_pass == password

@app.route('/', methods = ["GET"])
def index():
   input_pass = request.cookies.get('password')
   
   if logged_in(input_pass):
      files = [f for f in listdir('.') if isfile(join('.',f))]
   
      return render_template("index.html", files = files) 
   
   else:
      return render_template("login.html")
   
@app.route('/login', methods = ["POST"])
def login():
   input_pass = request.form.get('password')
   print(input_pass)
   resp = redirect('/')
   
   if logged_in(input_pass):
      resp.set_cookie('password', request.form.get('password'))
   return resp

@app.route('/file', methods = ["GET", "POST"])
def file():
   input_pass = request.cookies.get('password')
   
   if not logged_in(input_pass):
       return ""
   
   filename = request.args['filename']
   files = [f for f in listdir('.') if isfile(join('.',f))]
   if filename in files:
      return send_file(filename)
   else:
      return ""

if __name__ == '__main__':
   password = generate_random_password()
   print(password)
   print(get_local_ip())
   app.run(host='0.0.0.0', debug=True)
