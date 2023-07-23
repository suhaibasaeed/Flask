from flask import Flask, render_template
from helper import recipes, descriptions, ingredients, instructions

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", template_recipes=recipes)


# POST method is used to send data to the server via form
@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
    return render_template(
        "recipe.html",
        template_recipe=recipes[id],
        template_description=descriptions[id],
        template_ingredients=ingredients[id],
        template_instructions=instructions[id],
    )


@app.route("/about")
def about():
    return render_template("about.html")
