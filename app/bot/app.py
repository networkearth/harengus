import awsgi
 
from flask import Flask, render_template
from flaskext.markdown import Markdown
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
Markdown(app)

ENVIRONMENT = "" #"/Prod" # "/Stage"

@app.route("/index")
def index():
    return render_template('index.html', environment=ENVIRONMENT)

def lambda_handler(event, context):
    base64_content_types = ["image/png"]
    response = awsgi.response(app, event, context, base64_content_types)
    return response