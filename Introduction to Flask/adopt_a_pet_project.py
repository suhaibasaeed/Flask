from flask import Flask

# Create instance of Flask class and save as object called app
app = Flask(__name__)

# Create index route via function
# Use route decorator function to bind '/' URL path to the function
@app.route('/')
def index():
  """
  Return HTML element with text 'Adopt a pet'
  """
  return """
  <h1> Adopt a pet </h1>
  <p> Browse through the links below to find your new furry friend </p>
  """