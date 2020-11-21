from flask import Flask, render_template

app = Flask(__name__)

# Define route for the app's one and only page
@app.route("/")
def index():
    return render_template("index2.html")

app.run(host='0.0.0.0', port=80)


