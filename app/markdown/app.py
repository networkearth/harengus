import awsgi	
 
from flask import Flask, render_template
from flaskext.markdown import Markdown
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
Markdown(app)

@app.route("/index")
def stuff():
    return render_template('stuff.md')

#@app.route("/")
#def index():
#    return render_template('index.html')

def lambda_handler(event, context):
    return awsgi.response(app, event, context)