from flask import Flask
# Create instance of Flask object
app = Flask(__name__)

# Index route returns h1 tag with text
@app.route('/')
def index():
    return """
    <h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend:</p>
    <ul>
        <li>Dogs</li>
        <li>Cats</li>
        <li>Rabbits</li>
    </ul>
    """

app.run(debug=True, port=8000)