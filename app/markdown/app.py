import awsgi	
 
from flask import Flask, render_template, current_app
from flaskext.markdown import Markdown
from flask_bootstrap import Bootstrap

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response

app = Flask(__name__)
Bootstrap(app)
Markdown(app)

ENVIRONMENT = "/Prod" # "/Stage"

@app.route("/index")
def index():
    return render_template('index.md', environment=ENVIRONMENT)

@app.route("/meta")
def meta():
    return render_template('meta.md', environment=ENVIRONMENT)

@app.route("/ontology")
def ontology():
    return render_template('ontology.md', environment=ENVIRONMENT)

@app.route("/modeling")
def modeling():
    return render_template('modeling.md', environment=ENVIRONMENT)

def lambda_handler(event, context):
    base64_content_types = ["image/png"]
    response = awsgi.response(app, event, context, base64_content_types)
    return response