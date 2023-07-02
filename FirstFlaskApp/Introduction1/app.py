from flask import Flask
# Create instance of Flask class - pass in name of application which is special python variable
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'
