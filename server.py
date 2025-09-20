from flask import Flask


app = Flask(__name__)

@app.route('/')
def Home():
    print("If you see this the pipeline is working")
    return "First CI/CD with Flask on Render"
