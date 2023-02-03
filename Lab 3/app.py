from flask import Flask
app = Flask(__name__)

 #Lab 3
from flask import render_template, request
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return "Hello " + name
    return render_template("index.html")

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


from flask import render_template, request

@app.route("/form", methods=["GET", "POST"])
def form():
    form = NameForm()
    if request.method == "POST" and form.validate_on_submit():
        name = form.name.data
        return "Hello " + name
    return render_template("index.html", form=form)

app.config["SECRET_KEY"] = "your_secret_key"

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)

app.run()
