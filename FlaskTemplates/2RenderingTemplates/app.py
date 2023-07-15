from flask import Flask, render_template
from helper import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
  
  #### Return a rendered index.html file
  return ""

@app.route("/recipe/<int:id>")
def recipe(id):
    
  #### Return a rendered fried_egg.html file
  return ""