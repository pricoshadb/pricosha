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

# Home page where we'll display the site for now- maybe later we'll make a dedicated frontend
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return "ok"	
