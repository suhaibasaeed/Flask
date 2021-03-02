from flask import Flask, render_template, request
from helper import recipes, descriptions, ingredients, instructions, add_ingredients, add_instructions

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    # Variable used as key for new recipe data
    new_id = len(recipes) + 1
    # Makes sure there is data in form before trying to access them
    if len(request.form) > 0:
        #### Add the recipe name to recipes[new_id]

        #### Add the recipe description to descriptions[new_id]

        #### Add the values to new_ingredients and new_instructions
        new_ingredients = None
        new_instructions = None
        add_ingredients(new_id, new_ingredients)
        add_instructions(new_id, new_instructions)
    return render_template("index.html", template_recipes=recipes)


@app.route("/recipe/<int:id>")
def recipe(id):
    return render_template("recipe.html", template_recipe=recipes[id], template_description=descriptions[id],
                           template_ingredients=ingredients[id], template_instructions=instructions[id])


@app.route("/about")
def about():
    return render_template("about.html")