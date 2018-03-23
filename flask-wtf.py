from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config["SECRET_KEY"] = "Random"

# Inherit from the form class


class LoginForm(Form):
    username = StringField('username',  validators=[InputRequired(), Email()])
    password = PasswordField('password', validators=[InputRequired(), Length(min=5,max=10)])
    # date = DateField('entrydate', format="%Y-%m-%d")


@app.route("/", methods=["GET", "POST"])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return form.username.data
    # Pass the form into the template using the render template option
    return render_template("WTForm.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)