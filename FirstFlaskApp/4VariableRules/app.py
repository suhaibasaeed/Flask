from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello, World!</h1>'


@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
    return f"""
    <h2>Reporter {reporter_id} Bio</h2>
    <a href='/'>Return to home page</a>
    """
