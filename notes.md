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
    * Can be used to provide a default string or text if the variable doesn't exist
    * But doesn't work when template variable is equal to `None` or empty string
  * length
  * dictsort

### Inheritance
* Websites have some elements that exist on multiple webpages
  * E.g. navigation bar
  * Good use case for template
    * As opposed to having same nav bar in several different places
    * Having to change them in each place etc.
* E.g. of `base.html`
```
<html>
  <head>
    <title>MY WEBSITE</title>
  </head>
  <body>
  {% block content %}{% endblock %}
  </body>
</html>
```
* Our `index.html` will include `extends` keyword with name of template
  E.g.
```
{% extends "base.html"  %}
 
{% block content %}
    <p>This is my paragraph for this page.</p>
{% endblock %}
```
* Final rendered `index.html` template looks like below
```
<html>
  <head>
    <title>MY WEBSITE</title>
  </head>
  <body>
    <p>This is my paragraph for this page.</p>
  </body>
</html>
```
* Div element can be used for navigation bar
  * E.g.
```
<!DOCTYPE html>
<html>
  <body>
    <!-- Insert navigation bar HTML below -->
    <div>
  <a href="/">Recipes</a>
   | 
  <a href="/about">About</a>
</div>
    {% block content %}
    {% endblock %}
  </body>
</html>
```

## Flask Forms

### Introduction
* Forms allow us to get data from a user

### Flask Request Object
* A request is how clients and servers communicate
* Flask routes only support GET requests by default
  * POST allows us to send data i.e. through form
* To allow route handle POST requests: `@app.route("/", methods=["GET", "POST"])`
  * Even though GET is default we need to explicitly specify it to allow both
* We can get the form's data via flasks `request` object
  * Needs to be imported
  * Specifically **form** attribute
    * Which is dictionary with forms fields as keys
    * E.g. `text_in_field = request.form["my_text"]`

### Route Selection
* Flask route paths may change as sites become bigger
* We can use `url_for()` by passing in routes **function name** to get URL path
* E.g. for index function
```
@app.route('/')
def index:
```
  * Below 2 hyperlinks return same thing
```
<a href="/">Index Link</a>
<a href="{{ url_for('index') }}">Index Link</a>
```
  * We can still pass arguments to URL
```
  
```
  * Complete example
```
@app.route("/my_path/<int:my_id>"), methods=["GET", "POST"])
def my_page(my_id):
    # Access flask_name in this function
    new_variable = my_id
    ...
```

### FlaskForm Class
