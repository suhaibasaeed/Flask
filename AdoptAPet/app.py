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

    for pet in pets_list:
        html += f"<li>{pet['name']}</li>"

    html += "</ul>"

    return html


app.run(debug=True, port=8000)
