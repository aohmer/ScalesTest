from flask import Flask

app = Flask(__name__)

@app.route("/")
def ScalesTest():
    return "<h1>Scales Test</h1>" + "<p>This is a test page for the Scales application.</p>"