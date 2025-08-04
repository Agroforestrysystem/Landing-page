from flask import Flask, render_template, url_for
from profiles import team_members
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", members=team_members)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
