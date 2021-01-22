from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
  """Return HTML instead of plain text"""
  return '<h1>Hello, World!</h1>'

# Contains a link inside href which takes us back to the home page. Denoted by "/"
@app.route('/reporter')
def reporter():
    return """
    <h2>Reporter Bio</h2>
    <a href="/">Return to home page</a>
"""