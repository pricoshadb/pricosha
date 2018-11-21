from flask import Flask, render_template
from flaskext.mysql import MySQL
from helpers import *

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'suckingtoes'
app.config['MYSQL_DATABASE_DB'] = 'pricosha'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return "ok"	
