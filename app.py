from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect
from flask import url_for
import numpy as np
import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html" )

@app.route("/api", methods=["GET","POST"])
def api():
    if request.method == "POST":
        model = joblib.load('notebook.pkl')
        tweet = request.form["tweet"]
        prediction = list(model.predict([tweet]))[0]
        if prediction == 1:
            msg = "Oh boy! that is sarcastic!!"
            return render_template("index.html", msg=msg, tweet=tweet)
        else:
            error = "Ooops it's not a sarcasm!"
            return render_template("index.html", error=error, tweet=tweet)
    else:
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
