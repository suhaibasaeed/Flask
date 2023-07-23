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
* Another way to create a form but using a class
  * Gives us for mwith a submit button
  * Inherits from `FlaskForm`
  * E.g.
```
class MyForm(FlaskForm):
    my_textfield = StringField("TextLabel")
    my_submit = SubmitField("SubmitName")
```
  * Allows us to implement form as **template variables**
* Accessing of fields is done through Class attributes
  * E.g. of Flask app with form class
```
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
 
app = Flask(__name__)
# Protect from CSRF attacks
app.config["SECRET_KEY"] = "my_secret"
 
class MyForm(FlaskForm):
    # Label passed in as argument
    my_textfield = StringField("TextLabel")
    my_submit = SubmitField("SubmitName")
 
@app.route("/")
def my_route():
    # Instantitate class
    flask_form = MyForm()
    return render_template("my_template", template_form=flask_form)
```

### Template Form Variables
* We create form in template by acessing attributes of form passed into template
* E.g.
```
class MyForm(FlaskForm):
    my_textfield = StringField("TextLabel")
    my_submit = SubmitField("SubmitName")

my_form = MyForm()
 
return render_template(template_form=my_form)
```
  * Our template can look like the below
```
<form action="/" method="post">
    {{ template_form.hidden_tag() }} # Handles necessary tasks for CSRF attacks
    {{ template_form.my_textfield.label }} # Get label of field
    {{ template_form.my_textfield() }} # Field itself
    {{ template_form.my_submit() }}
</form>
```
  * Rendered HTML
```
<form action="/" method="post">
    <input id="csrf_token" name="csrf_token" type="hidden" value="ImI1YzIxZjUwZWMxNDg0ZDFiODAyZTY5M2U5MGU3MTg2OThkMTJkZjQi.XupI5Q.9HOwqyn3g2pveEHtJMijTu955NU">
    <label for="my_textfield">TextLabel</label>
    <input id="my_textfield" name="my_textfield" type="text" value="">
    <input id="my_submit" name="my_submit" type="submit" value="SubmitName">
</form>
```

### Handling FlaskForm Data
* POST request allows submitted form data to be sent to server
  * We can get this data from the form instance via **data atrribute**
  * E.g. `form_data = flask_form.my_textfield.data`
* Remember to add POST request to route decorate E.g. `methods=["GET", "POST"]`

### Validation
* Used to check things like if data is populated or in correct format
* Done in form class using `validators` parameter in form field **definition**
* E.g. below makes field require it to actually have something in there
  * Handles user notification for us
```
from wtforms.validators import DataRequired

my_textfield = StringField("TextLabel", validators=[DataRequired()])
```
* A way of checking for valid form submission is using `validate_on_submit()`
  * Returns True if all associated form validators are ok
  * If it returns False then route function can just move on to rendering template etc
  * E.g. 
```
if my_form.validate_on_submit():
    # get form data
```

### More Form Fields
* WTForms also supports other objects for form fields
* **TextAreaField** - Supports multi-line input
  * E.g. `my_text_area = TextAreaField("Text Area Label")`
* **BooleanField** - Allows us to create a checkbox element
  * Data returned is either True or False
  * E.g. `my_checkbox = BooleanField("Checkbox Label")`
* **RadioField** - Allows us to create radio button group
  * 1st argument is label and also has keyword arg called `choices` which is list of tuples
    * Each tuple is for a button
      * Button ID string and label string
  * We usually need to loop through `RadioField` to get the components
  * E.g. `my_radio_group = RadioField("Radio Group Label", choices=[("id1", "One"), ("id2","Two"), ("id3","Three")])`
* Good practice is to define forms in separate file like **forms.py**

### Redirecting
* The `redirect()` function allows us to move from one route to another
  * Example situation: we create form in one route but after **form submission** want to end up in another route
  * E.g. `redirect("url_string")`
  * Good to use after we have processed and saved data within `validate_on_sumbit` check
  * Allows us to avoid code duplication
* We can also use it in conjunction with `url_for()` so we can specify the function name instead
  * Prevents URL string pitfalls
  * E.g. `redirect(url_for("new_route", _external=True, _scheme='https'))`
    * Ensures we re-direct to HTTPS instead of HTTP
  * We still have option of using keywork args: `redirect(url_for("new_route", new_var=this_var, _external=True, _scheme='https'))`