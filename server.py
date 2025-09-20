from flask import Flask


app = Flask(__name__)

@app.route('/')
def Home():
    # NOTE: This print statement will NOT appear in the browser.
    # It will be visible only in the Render "Logs" tab.
    print("If you see this the pipeline is working")
    return "First CI/CD with Flask on Render"
