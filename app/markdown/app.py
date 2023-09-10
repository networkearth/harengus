import awsgi	
 
from flask import Flask, render_template
from flaskext.markdown import Markdown
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
Markdown(app)

@app.route("/index")
def index():
    return render_template('index.md')

@app.route("/meta")
def meta():
    return render_template('index.md')

@app.route("/ontology")
def ontology():
    return render_template('index.md')

@app.route("/modeling")
def modeling():
    return render_template('index.md')

#@app.route("/")
#def index():
#    return render_template('index.html')

def lambda_handler(event, context):
    return awsgi.response(app, event, context)