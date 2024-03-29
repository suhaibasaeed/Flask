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

### Declaring Relationships - Foreign Keys
* To complete our one-to-many relation we also need to specify **foreign keys** for model on **many** side
* Foreign key is field in table that references **primary key** in another table
* In above example the relationships in opposite direction are as follows
  * A single review can only be for one book
  * A single review can only be done by one reader
* E.g. We need to specify the primary key for `Book` table in Foreign key field
  * `book_id = db.Column(db.Integer, db.ForeignKey('book.id'))`
    * `book.id` is Primary key of Book table but book_id is foreign key field

### Initialising DB
* The previous code doesn't intialise DB according to declared models
  * To do this run code below
```
python
>>> from app import db
>>> db.create_all() # After this DB schema and myDB.db DB file created as per URI config field
```

### Creating DB Entries
* SQLAlchemy ORM (Object Relational Mapper) allows us to create DB entries as instances of Class (objects)
* E.g.
```
from app import Reader, Book, Review
b1 = Book(id = 123, title = 'Demian', author_name = 'Hermann', author_surname = 'Hesse', month = "February", year = 2020)
r1 = Reader(id = 342, name = 'Ann', surname = 'Adams', email = 'ann.adams@example.com')
```
* We interact with DB entries as normal python objects
  * E.g `print("My first reader:", r1.name) # prints My first reader: Ann`

### Creating DB Entries - Relationships
* Creating objects for tables that have foreign keys is a little different
  * As we need to set the foreign keys that reference primary keys in other tables
* E.g. with Review table
```
b1 = Book(id = 123, title = 'Demian', author_name = 'Hermann', author_surname = 'Hesse')
b2 = Book(id = 533, title = 'The stranger', author_name = 'Albert', author_surname = 'Camus')
r1 = Reader(id = 342, name = 'Ann', surname = 'Adams', email = 'ann.adams@example.com')
r2 = Reader(id = 312, name = 'Sam', surname = 'Adams', email = 'sam.adams@example.com')

rev1 = Review(id = 435, text = 'This book is amazing...', stars = 5, reviewer_id = r1.id, book_id = b1.id)
```
* **If we don't explicitly set primary key it's auto created for us when adding entry to DB**

## DBs in Flask - Reading, Updating & Deleting

### Queries - query.all() and query.get()
* To query DB table in Flask with SQLAlchemy we use `.query attr`
  * E.g. `TableName.query.all()` gives us all entries from model
  * If we know the primary key of entry we need we can use `.get()` method instead `TableName.query.get(123)`
    * We can then access attributes
* ORM allows us to essentially treat DB table as **class** and DB rows and **objects**
  * E.g.
```
readers = Reader.query.all()
for reader in readers: 
    print(reader.name)

```

### Queries: Retreive Related Objects
* To get related objects of an object we can access the attribute we defined with `.relationship()` method
  * E.g. to get all reviews of the reader with ID 123
```
reader = Reader.query.get(123)
reviews_123 = reader.reviews.all()
```
  * reviews attr was defined in Reader model column: `reviews = db.relationship('Review', backref='reviewer', lazy = 'dynamic')`
* To fetch a single object we can use the `backref` field in the `relationship()`
  * E.g. For `Review` object we can get authoring `Reader` as below
```
review = Review.query.get(111)
reviewer_111 = review.reviewer
```
  * Or another way to do the above would be: reviewer_111 = `Review.query.get(111).reviewer`
    * One review has one reader/reviewer
  * We could acheive the same using .all() too as one reader can have many reviews: `reviews_123 = Reader.query.get(123).reviews.all()`

### Queries: Filtering
* Sometimes we may only want specific entries and not all
  * We can use .filter() method for this
    * But we still use `query` attr
    * Returns `Query` object which we need to do additional methods on
  * E.g. get books from `Book` table from year 2020
    * `Book.query.filter(Book.year == 2020).all()`
      * Instead of `all()` we could do `.first()` or `.count()`
* We can also specify **multiple criteria** by separating them via **comma** that acts as AND operator
  * E.g. below teturns all reviews with a start rating of 3 and above for the book with ID 1
  * `Review.query.filter(Review.stars <= 3, Review.book_id == 1).all()`
* Another option is `filter_by()` method which usses attribute-value for filtering

### Queries: Advanced Filtering
* More complex queries like checking if column starts or neds with string are also possible
  * E.g.
    *  Get emails that end with `edu` - `education = Reader.query.filter(Reader.email.endswith('edu')).all()`
    * Use `.like()` method to get readers with emails that have `.` before @ sign in email: `emails = Reader.query.filter(Reader.email.like('%.%@%')).all()`
      * `%` represents 0/1/multiple characters
* We can also order the returned results by using `order_by()` method on `query` attr
  * E.g. `ordered_books = Book.query.order_by(Book.year).all()`
  
### Session - Add & Rollback
* DB transactions include additions, removals and updating of DB entries
* DB **session** entails one or more transaction
  * **Comitting** ends transaction by saving it to DB permanently - done via `.commit()` method
    * Rollback rejects pending transactions
* In Flask-SQLAlchemy DB is changed in context of sessions
  * Uses `session` atr of DB instance
    * Entry added to session via `.add()` method
* E.g below creates new Reader entries and tries to add to DB.
  * 2nd reader will fail as info is duplicated from 1st - Try allows us to gracefully rollback and continue code execution
```
from app import db, Reader
new_reader1 = Reader(name = "Nova", surname = "Yeni", email = "nova.yeni@example.com")
new_reader2 = Reader(name = "Nova", surname = "Yuni", email = "nova.yeni@example.com")
new_reader3 = Reader( name = "Tom", surname = "Grey", email = "tom.grey@example.edu")

db.session.add(new_reader1)
try:
    db.session.commit()
except:
    db.session.rollback()
```

### Session: Updating Existing Entries
* Sometimes we might just want to update value in an existing column entry
  * E.g. we change email address of a reader with id of 3
```
reader = Reader.query.get(3)
reader.email = “new_email@example.com”
db.session.commit()
```

### Session: Removing DB Entries
* We need to be careful with one-to-many relationships when removing
  * Removing a reader we would think that their reviews are also deleted
  * Similarly removing a book we would think would also remove the reviews for it
    * Called **cacading deletion**
  * The way we defined our models this **would not** happen by default
    * So we would need to enable this when defining the models initially
      * Done by adding `cascade` parameter to `.relationship` field of `Reader` and `Book`
        * As below
        * reviews = db.relationship('Review', backref='reviewer', lazy='dynamic', cascade = 'all, delete, delete-orphan')
      * In practice we'd need to migrate/re-init DB to change this
* On the other hand removing a review doesn't affect `Book` and `Reader` tables in cascading way
* To remove a reader with ID of 753: `db.session.delete(Reader.query.get(753))`
  * All of their reviews are deleted as well

### Queries and Templates
* We can combine jinja2 template with DB queries in our routes
```
@app.route('/books/<year>')
def books(year):
   books = Book.query.filter_by(year = year)
   return render_template('display_books.html', year = year, books = books)
```
* We can also sue the `.first_or_404()` method to gracefully handle any DB query failures
  * It returns HTTP 404 not found response code
  * E.g. `reader = Reader.query.filter_by(id = user_id).first_or_404(description = "There is no user with this ID.")` 