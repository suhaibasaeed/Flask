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
    Return HTML element with unordered list of each pet type
    """
    html = f"<h1> List of {pet_type}</h1>"
    html += "<ul>"
    # Loop through list of pet types and create links for them based on their ID
    for count, i in enumerate(pets[pet_type]):
        new_html = f"<li><a href= /animals/{pet_type}/{count}>{i['name']}</a></li>"
        html += new_html
    html += "</ul>"

    return html


# Create and link individual profile pages for each pet
@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    """
    Return HTML element with the pets name, image, description and unordered list with breed and age
    """
    # Get pet dictionary from the pets dictionary
    pet = pets[pet_type][pet_id]

    return f"""
  <h1> {pet['name']} </h1>
  <img src={pet['url']} />
  <p> {pet['description']} </p>
   <ul>
    <li>Breed: {pet['breed']}</li>
    <li>Age: {pet['age']}</li>
  </ul>
  """
