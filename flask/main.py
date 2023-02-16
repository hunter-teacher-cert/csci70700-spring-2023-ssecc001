from flask import Flask
import random
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Welcome to Ms. Seccaficos Website</h1>' 
  
@app.route('/about')
def about():
  return render_template("about.html")
@app.route('/episode')
def episode():
  number = random.randrange(1,6)
  number1 = random.randrange(1,26)
  return render_template("episode.html",num=number,num1=number1)




  
app.run(host='0.0.0.0', port=81)

