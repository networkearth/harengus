import awsgi
import openai
import boto3
import json
 
from flask import Flask, render_template, request
from flaskext.markdown import Markdown
from flask_bootstrap import Bootstrap

def get_secret(secret_name, region_name):
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except Exception as e:
        # Handle exceptions as appropriate for your application needs
        print(f"Error retrieving secret: {str(e)}")
        return None

    # Depending on whether the secret is a string or binary, one of these fields will be populated
    if 'SecretString' in get_secret_value_response:
        secret = get_secret_value_response['SecretString']
        return json.loads(secret)
    else:
        # If the secret is binary, decode it and return as appropriate for your use case
        binary_secret_data = get_secret_value_response['SecretBinary']
        return binary_secret_data.decode()

app = Flask(__name__)
region_name = "us-east-1"
secret_name = "harengus_openai_api_key"
secrets = get_secret(secret_name, region_name)
app.config["OPENAI_API_KEY"] = secrets.get("OPENAI_API_KEY")

Bootstrap(app)
Markdown(app)

ENVIRONMENT = "/Prod"

@app.route("/index", methods=["GET"])
def index_get():
    messages = [
        {"role": "assistant", "content": "Hello, how can I help you?"},
    ]
    return render_template('index.html', environment=ENVIRONMENT, messages=messages)

@app.route("/index", methods=["POST"])
def index_post():
    user_message = request.form.get("user_message")
    previous_messages = request.form.getlist("messages")
    
    messages = []
    for message in previous_messages:
        user, text = message.split(": ", 1)
        messages.append({"role": user, "content": text})
    messages.append(
        {"role": "user", "content": user_message}
    )
    
    # Querying ChatGPT
    openai.api_key = app.config["OPENAI_API_KEY"]
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=messages,
        temperature=0.6,
        max_tokens=150,
    )
    
    agent_response = response["choices"][0]["message"]["content"].strip()
    messages.append({"role": "assistant", "content": agent_response})

    return render_template('index.html', environment=ENVIRONMENT, messages=messages)

def lambda_handler(event, context):
    base64_content_types = ["image/png"]
    response = awsgi.response(app, event, context, base64_content_types)
    return response