from flask import Flask  # import Flask class

# Create instance of Flask class and pass in name of app
# Value of __name__ depends if this file is executed or imported as a module
app = Flask(__name__)

print(__name__)