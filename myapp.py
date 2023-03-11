from flask import Flask, render_template
from flask_wtf import Flaskform
from wtforms import StringField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret string"

class MyForm(Flaskform):
    myfield = StringField("Email", validators=[DataRequired(), Email()])


@app.route('/<name>', methods=["GET", "POST"])
def hello(name=None):
    my_form = MyForm()
    if my_form.validate_on_submit():
        mydata = my_form.my_field.data
        return redirect("anotherroute", data=mydata)
    return render_template('index.html', name=name, template_form=my_form)

if __name__ == '__main__':
    app.run()
