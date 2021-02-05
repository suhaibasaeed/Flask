from flask import Flask
from helper import pets

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
    <li><a href= '/animals/dogs'>Dogs</a></li>
    <li><a href= '/animals/cats'>Cats</a></li>
    <li> <a href= '/animals/rabbits'>Rabbits</a></li>
  </ul>
  """


# Function which will return individual pages for animal types and link them in the list
# Use route decorator function to bind '/animals/pet_type' URL path to the function
@app.route('/animals/<string:pet_type>')
def animals(pet_type):
    """
  Return HTML element with header 'List of pets'
  """
    html = f"<h1> List of {pet_type}</h1>"
    html += "<ul>"
    for i in pets[pet_type]:
        new_html = f"<li> {i['name']} </li>"
        html += new_html
    html += "</ul>"

    return html


@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_id):
  pass