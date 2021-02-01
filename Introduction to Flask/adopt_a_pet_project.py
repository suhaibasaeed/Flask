from flask import Flask

# Create instance of Flask class and save as object called app
app = Flask(__name__)

# Create index route via function
# Use route decorator function to bind '/' URL path to the function
@app.route('/')
def index():
  """
  Return HTML element with text 'Adopt a pet', paragraph and an unordered list of animals
  """
  return """
  <h1> Adopt a pet </h1>
  <p> Browse through the links below to find your new furry friend </p>
  <ul>
    <li>Dogs</li>
    <li>Cats</li>
    <li>Rabbits</li>
  </ul>
  """

# Function which will return individual pages for animal types and link them in the list
# Use route decorator function to bind '/animals/pet_type' URL path to the function
@app.route('/animals/<string:pet_type>')
def animals(pet_type):
  """
  Return HTML element with header 'List of pets'
  """
  html = "<h1> List of pet </h1>"

  return html
