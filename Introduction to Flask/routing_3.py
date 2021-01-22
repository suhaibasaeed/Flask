from flask import Flask

app = Flask(__name__)

# Use route() decorator to bind URL to view function
# Function will be triggered when the specified URL is visited
@app.route('/')  # URL path passed in as parameter
@app.route('/home')
def home():
  """View function for processing request and generating response"""
  return "Hello, World!"

@app.route('/reporter')
def reporter():
  return "Reporter Bio"
