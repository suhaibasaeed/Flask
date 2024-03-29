from flask import Flask, render_template
from helper import recipes, descriptions, ingredients, instructions

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipe/<int:id>")
def recipe(id):
    return render_template(
        "recipe.html",
        template_recipe=recipes[id],
        template_ingredients=ingredients[id],
        template_instructions=instructions[id],
        template_description=descriptions[id],
    )
