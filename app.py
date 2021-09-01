from flask import Flask,render_template, requests
from flask.wrappers import Response
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="tcc",
  password="pass",
  database='assign'
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/details')
def det_form():
    return render_template('web.html')
 
@app.route('/push', methods = ['POST', 'GET'])
def register(): 
    if request.method == 'GET':
        return "Success"
     
    if request.method == 'POST':
        usr = request.det_form['user']
        inc_webhook = request.det_form['webhook']
        type = request.det_form['type']
        sql_query = "INSERT INTO registry (usr, inc_webhook, type) VALUES (%s, %s, %n)"
        values = (usr, inc_webhook, type)
        mycursor.execute(sql_query, values)
        mydb.commit()
        return "Store Success"
 
app.run(host='localhost', port=54321)
