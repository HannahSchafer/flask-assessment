from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import sample

app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"




@app.route("/")
def start_here():
    """Homepage"""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Go to application form."""

    jobs = ["Software Engineer", "QA Engineer", "Product Manager"]
    
    return render_template("application-form.html", jobs=jobs)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
