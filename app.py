from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "q"


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    message = TextAreaField(label='Message')
    submit = SubmitField('Send')


@app.route("/")
def index():
    return render_template("index2.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    return render_template("contact.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
