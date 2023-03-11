from flask import Flask, render_template
from flask_wtf import Flaskform
from wtforms import StringField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)

class MyForm(Flaskform):
    myfield = StringField("Email", validators=[DataRequired(), Email()])


@app.route('/<name>', methods=["GET", "POST"])
def hello(name=None):
    my_form = MyForm()
    if my_form.validate_on_submit():
        mydata = my_form.my_field.data
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()
