# Flask

## Build Your First Flask App

### Routing
* We can create **endpoints** in our app to handle different requests
  * Done via **view functions**
    * Processes request and generates response
      * E.g. text
  * `route()` decorator binds URL to view function
    * Triggers when URL is hit
    * Path taken as parameter
      * Multiple URLs can be bound to same view function

### Render HTML
* Possible to return HTML instead of string in view function
  * E.g.
```
@app.route('/')
@app.route('/home')
def home():
    return '''
    <h1>Hello, World!</h1>
    <p>My first paragraph.</p>
    <a href="https://www.codecademy.com">CODECADEMY</a>
    '''
```

### Variable Rules
* Allows us to create dynamic URLs that change
* We specify varibles within a URL using <xxx>
  * E.g. `<variable_name`
* These variables will also need to be passed in as **arguments** to view function
* E.g.
```
@app.route('/orders/<user_name>/<int:order_id>')
def orders(user_name, order_id):
    return f'<p>Fetching order #{order_id} for {user_name}.</p>
```
* We can also **enforce** types of variables being accepted
  * But optional
  * Possible types:
    * string - accepts any text without a slash **(default)**
    * int - accepts positive integers
    * float - accepts positive floating point values
    * path - like string but also accepts slashes
    * uuid - accepts UUID strings

## Flask Templates

### Rendering Templates
* We use built in `render_template()` to render a html or jinja2 template
  * Pass in name of template
  * Looks for templates in the `templates/` directory
* E.g.
```
from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html")
```

### Template Variables
* We can also pass variables to `render_template()` function
  * E.g.
```
flask_variable = "Text for my template"
 
render_template("my_template.html", template_variable=flask_variable)
```
* Possible to use keyword args too

### Variable Filters
* Jinja2 filters allows us to modify a variables output
* E.g.
```
{{ template_heading |  title }}
 
OUTPUT
My Very Interesting Website
```
* Other examples of filters
  * lower
  * default
  * length
  * dictsort
