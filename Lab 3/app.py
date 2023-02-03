from flask import Flask
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config["SECRET_KEY"] = "your_secret_key"

class NameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/form", methods=["GET", "POST"])
def form():
    form = NameForm()
    if request.method == "POST" and form.validate_on_submit():
        name = form.name.data
        return "Hello " + name
    return render_template("form.html", form=form)

app.run()

csrf = CSRFProtect(app)


