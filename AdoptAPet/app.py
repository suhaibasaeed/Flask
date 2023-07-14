from flask import Flask
from helper import pets

# Create instance of Flask object
app = Flask(__name__)


# Index route returns h1 tag with text
@app.route("/")
def index():
    return """
    <h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend:</p>
    <ul>
        <li><a href='/animals/dogs'>Dogs</a></li>
        <li><a href='/animals/cats'>Cats</a></li>
        <li><a href='/animals/rabbits'>Rabbits</a></li>
    </ul>
    """


@app.route("/animals/<pet_type>")
def animals(pet_type):
    html = f"<h1>List of {pet_type}</h1>"

    html += "<ul>"

    pets_list = pets[pet_type]

    for index, pet in enumerate(pets_list):

        html += f"<li><a href='/animals/{pet_type}/{index}'>{pet['name']}</a></li>"

    html += "</ul>"

    return html


@app.route("/animals/<pet_type>/<int:pet_id>")
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]

    return f"""<h1>{pet['name']}</h1>
    <img src='{pet['url']}'/>
    <ul>
        <li>Age: {pet['age']}</li>
        <li>Breed: {pet['breed']}</li>
    </ul>
    """


app.run(debug=True, port=8000)
