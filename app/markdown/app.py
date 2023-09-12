import awsgi	
import json
 
from flask import Flask, render_template
from flaskext.markdown import Markdown
from flask_bootstrap import Bootstrap

import plotly
import plotly.express as px
import pandas as pd

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

@app.route("/concern")
def concern():
    return render_template('concern.md', environment=ENVIRONMENT)

@app.route("/biomass")
def biomass():
    return render_template('biomass.md', environment=ENVIRONMENT)

@app.route('/notdash')
def notdash():
   df = pd.DataFrame({
      'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 
      'Bananas'],
      'Amount': [4, 1, 2, 2, 4, 5],
      'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
   })
   fig = px.bar(df, x='Fruit', y='Amount', color='City', 
      barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('notdash.html', graphJSON=graphJSON)

def lambda_handler(event, context):
    base64_content_types = ["image/png"]
    response = awsgi.response(app, event, context, base64_content_types)
    return response