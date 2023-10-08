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


## SQL - Manipulation

### Introduction to SQL
* SQL uses declarative statements
* SQLite RDBMS used

### Relational Databases
* Relational DBs organise info into table/s
* A table is a **collection** of data
  * Organised into rows and columns
* Data types
  * **INTEGER** - Positive/Negative number
  * **TEXT** - String
  * **DATE** - Formatted as YYYY-MM-DD E.g. '1940-05-30'
  * **REAL** - Decimal
  
### Statements
* SQL **statement** is text the DB sees as **valid command**
  * Always end in semicolon
* Doesn't matter if statement is on one line or multiple
* E.g.
```
CREATE TABLE table_name (
   column_1 data_type, 
   column_2 data_type, 
   column_3 data_type
);
```
  * `CREATE TABLE` - Clause which does specfic task
    * Always written in capitals
  * `table_name` - Name of table to apply command to
  * `(column_1 data_type, column_2 data_type, column_3 data_type)` - Parameter - Essentially list of column names with corresponding data type

### Create
* `CREATE` statements are used to create **new tables** in DB
* E.g.
```
CREATE TABLE celebs (
   id INTEGER, 
   name TEXT, 
   age INTEGER
);
```
  * celebs is name of table
  * 3 columns in DB - `id`, `name` & `age`

### Insert
* `INSERT` statements adds **new row** to table
* E.g.
```
INSERT INTO celebs (id, name, age) 
VALUES (1, 'Justin Bieber', 22);
```
  * `INSERT INTO` - Clause to add specific row/rows
  * `(id, name, age)` - paramater to identify columns to add data into
  * `VALUES` - Clause to indicate data to insert
  * `(1, 'Justin Bieber', 22)` - Parameter identifying values to insert
    * INTEGER, TEXT and INTEGER respectively

### Select
* Used to **fetch data** from DB
* To return all data in `name` column of `celebs` table: `SELECT name FROM celebs;`
* Or we could returns all column using wildcard character `*`: `SELECT * FROM celebs;`

### Alter
* `ALTER TABLE` allows us to add **new column** to table
* Example below adds new column `twitter_handle` to `celebs` table
```
ALTER TABLE celebs 
ADD COLUMN twitter_handle TEXT;
```
  * All rows that existed before column was added will have `NULL` (∅) value for them

### Update
* **Edits** row in table - i.e. existing record
* Example below changes record with id = 4 to have `twitter_handle` of `@taylorswift13`
```
UPDATE celebs 
SET twitter_handle = '@taylorswift13' 
WHERE id = 4; 
```
  * `WHERE` is clause used to indicate **which row** we want to update

### Delete
* `DELETE FROM` statement allows us to delete existing row/s
* Below example deletes all rows in `celebs` table where the `twitter_handle` column is **blank**
```
DELETE FROM celebs 
WHERE twitter_handle IS NULL;
```
  * `IS NULL` is SQL condition that returns TRUE when value is `NULL` and FALSE otherwise


### Constraints
* Constraints allow us to add info about how column can be used
  * Done **after** specifying **type**
  * Can be used to tell DB to reject data that doesn't adhere to specific rule
* Example below sets contraints on celebs table
```
CREATE TABLE celebs (
   id INTEGER PRIMARY KEY, 
   name TEXT UNIQUE,
   date_of_birth TEXT NOT NULL,
   date_of_death TEXT DEFAULT 'Not Applicable'
);
```
  * `PRIMARY KEY` column used to uniquely ID row
    * If we tried to add a new row with identical value it would not work
    * **Table can only have one primary key field**
  * `UNIQUE` columns have different values for each row
    * Unlike primary keys we can have **multiple** columns in a table
  * `NOT NULL` columns must have a value inside them
    * If we tried to create one with nothing in it then it wouldn't work
  * `DEFAULT` columns take an argument which allow us to specify default value
    * If we don't specify a value for it


## Queries

### Select
* We can focus on a few columns in a table using `SELECT` statement
* E.g.
```
SELECT column1, column2 
FROM table_name;
```

### As
* `AS` keyword allows us to give **alias** to a column
  * Recommended to do this in **single quotes**
  * PostgreSQL can require double quotes or even no quotes
* Original column name **doesn't change**
* E.g
```
SELECT name AS 'Titles'
FROM movies;
```

### Distinct
* The `DISTINCT` keyword allows us to return **only unqiue values** in a column
  * Any duplicated rows are filtered out
* E.g.
```
SELECT DISTINCT tools 
FROM inventory;
```

### Where
* Allows us to filter query results using a condition
* We can use **comparsion operators** with `WHERE` clauses
  1. Equal to - =
  2. Not equal to - !=
  3. Greater than - >
  4. Less than - <
  5. Greater than or equal to - >=
  6. Less than or equal to<=
* E.g.
```
SELECT *
FROM movies
WHERE imdb_rating > 8;
```

### Like
* `LIKE` operator allows us to **compare** similar values
  * Used in conjection with `WHERE`
* In e.g. below we want to get all movies that start with `se` and end in `en` with one character in between
```
SELECT * 
FROM movies
WHERE name LIKE 'Se_en';
```
  * `Se_en` is a pattern with `_` meaning any character

### Like II
* `%` is also wildcard character which can be used with `LIKE`
* Example below only includes movies where the name begins with the letter `A`
```
SELECT * 
FROM movies
WHERE name LIKE 'A%';
```
* Essentially matches 0+ missing letters in pattern
  * E.g. `%a` matches all movies with end in letter `a`
* It's possible to use `%` **both** before and after pattern
  * In E.g. below any movie with `man` in it's name will be returned
  * Will match both `Batman` and `Man of Steel` as `LIKE` is **NOT case sensitive**
```
SELECT * 
FROM movies 
WHERE name LIKE '%man%';
```

### Is Null
* Unknown values are usually displayed as `NULL` value
* We can use the `IS NULL` & `IS NOT NULL` operators with these
* Example below get's all movies that have an IMDB rating
```
SELECT name
FROM movies 
WHERE imdb_rating IS NOT NULL;
```

### Between
* Allows us to filter results **within range** when used alongside `WHERE` clause
  * E.g. below returns movies which have a year value of 1990 - 1999 inclusive
```
SELECT *
FROM movies
WHERE year BETWEEN 1990 AND 1999;
```
* If value is text then `BETWEEN` filters based on alphabetical range
  * But 2nd value **NOT included** unless value is that letter only
  * In e.g. below the results will include movie whose names start with letter between A - I
    * Unless the name is `J` only
    * `Jaws` would not be returned but `J would`
```
SELECT *
FROM movies
WHERE name BETWEEN 'A' AND 'J';
```

### And
* `AND` operator allows to **combine multiple conditions** alongside `WHERE` clause
  * Both conditions need to be True
* Example berlow returns movies with the genre `romance` with a `year` value during the 90's
```
SELECT * 
FROM movies
WHERE year BETWEEN 1990 AND 1999 AND genre = 'romance';
```

### Or
* `OR` operator conversely will return results where **at least one** condition is True
* E.g.
```
SELECT *
FROM movies
WHERE year > 2014
   OR genre = 'action';
```

### Order By
* Allows us to sort results
  * Could be numerically or alphabetically
  * Either in **ascending** or **descending** order
* In e.g. below we sort by name column alphabetically in ascending order
```
SELECT *
FROM movies
ORDER BY name;
```
* To order in descending order use `DESC`
  * E.g.
```
SELECT *
FROM movies
WHERE imdb_rating > 8
ORDER BY year DESC;
```
  * `ASC` is ascending
* **Column we're sorting on doesn't have to be one we display**
* If we're using `WHERE` clause `ORDER BY` always has to come **after it**

### Limit
* Sometimes we may have large tables and want to **limit** amount of data returned.
  * Also allows queries to **run faster**
* `LIMIT` clause allows us to specify **max no. of rows** returned
* E.g.
```
SELECT *
FROM movies
ORDER BY imdb_rating DESC LIMIT 3;
```
* Clause always **goes at end** and isn't supported by all DBs

### Case
* Essentially allows us to do if-then logic in SQL
* E.g.
```
SELECT name,
 CASE
  WHEN imdb_rating > 8 THEN 'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid at All Costs'
 END
FROM movies;
```
  * We want to rank ratings using 3 levels
    * rating > 8 - Fantastic
    * rating > 6 - Poorly Received
    * Else: Avoid at All Costs
    * `THEN` gives us new column in query result
    * `CASE` statement **must end** with `END`
  * In e.g. above we can rename new column using `END AS` instead of `END`


## SQLite

* Very popular DB engine
  * i.e. software that allows users to interact with RDB
* Stores DB in **single file**
  * Makes copying and sharing DB very easy
* Allows DB use without server application
* DB on same disk as app

### Drawbacks
* Makes multiple concurrant updates impossible
  * Only one user can write to file at same time
* Security
* Missing advanced features that other DB systems have
* No validation of data types
  * Allows data of any type to be in any column
    * Still uses schemas but doesn't enforce it

### DB Browser
* Visual tool that is used to organise commands sent to SQLite
  * Also allows you to view column structure of tables
* Can be used to visualise what SQL command will do without actually affecting DB
  * Changes can be commited once we're happy


## INTRODUCTION TO FLASK-SQLALCHEMY

### Why Have Databases in Your Web Applications
* DB data organised into entities that are related
  * E.g. Users related to products by purchasing
  * Albums related to artist by authoring
* DBs consist of tables that represent entities and their relationships
* Entity **attributes** are **constrained**
  * E.g. NAME attr is string or PASSWORD has to be non-empty
* All of this defined in DB **schema**
  * Without any data
* Schema Design - Book Club Scenario
  * Each month we chose book for friends to rate/review
  * App manages readers, list of books chosen and their ratings
  * **Entities**
    * `Reader`, `Bool`, `Review`, `Annotation`
      * One table for each
  * **Attributes** - Properties of entity
    * E.g Attrs of `Reader` are NAME, SURNAME and EMAIL
  * **Relationships**
    * Readers are in relationships with books by reading and annotating them.
      * A reader can read and annotate multiple books
      * A single book can can many reviews and annotations

### Flask Application with Flask-SQL-Alchemy
* Flask extension that supports use of Python SQLAlchemy SQL Toolkit
* We need to specify DB URL
  * `app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'`


### Declaring a Simple Model - Book
* `db` object has all functions/helpers from SQLAlchemy and ORM
  * ORM associates and user-defined **Classes** with **DB tables** for us
    * As well as instances of the classes with DB tables
    * Classes that mirror a DB table are called **models**
* To declare a model we inherit from `db.Model` Class which is **declarative base** in SQLAlchemy
  * E.g.
```
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column, automatically generated IDs
    title = db.Column(db.String(80), index = True, unique = True) # book title
    author_surname = db.Column(db.String(80), index = True, unique = False) #author surname
    month = db.Column(db.String(20), index = True, unique = False) #the month of book suggestion
    year = db.Column(db.Integer, index = True, unique = False) #the year of book suggestion
```
  * `Book` model has 5 attributes of columns class 
    * **Type** is first argument e.g. String
    * Column class can also take other params
      * `unique` - Values in column must be unique when True
      * `index` - Column searchable by values when True
      * `primary_key` - column is primary key when True

### Declaring One-to-Many Relationships
* In SQLAlchemy relationships declared via `.relationship()` method
* In our case we have one book with many reviews
  * Plus one reader with many reviews
  * Thus we add relationship field to `Book` and `Reader` models via below
    * `reviews = db.relationship('Review', backref='book', lazy='dynamic')`
      * First argument is for which model is on **many side** or relationship (Review)
      * `backref = 'book'` puts `book` attr in `Review` Class that refers back to **Book object**
      * `lazy = dynamic` means related objects load as **SQLAlchemy query objects**
      * **This only covers one side in relationship - i.e. one book to many reviews and not other side**

