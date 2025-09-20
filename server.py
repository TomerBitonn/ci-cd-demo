from flask import Flask


app = Flask(__name__)

@app.route('/')
def Home():
    return "My first CI/CD with Flask on Render"
