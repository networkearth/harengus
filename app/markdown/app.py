import awsgi	
 
from flask import Flask, render_template
from flaskext.markdown import Markdown
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
Markdown(app)

@app.route("/stuff")
def stuff():
    return render_template('stuff.md')

def lambda_handler(event, context):
    return awsgi.response(app, event, context)