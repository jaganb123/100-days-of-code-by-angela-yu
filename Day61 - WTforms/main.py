from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_bootstrap import Bootstrap

class MyForm(FlaskForm):
    # name = StringField('name', validators=[DataRequired()])
    def email_validate(form, field):
        if not ( '@' in field.data and '.' in field.data ):
            raise ValidationError('Invalid Email address')


    email = EmailField(label='Email', validators=[DataRequired(), email_validate])

    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)], )
    submit = SubmitField(label='login1')

def check_login_cred(email, password):
    userEmail = ['admin@email.com']
    userPassword = ['12345678']
    if email in userEmail and password in userPassword:
        return True
    else:
        return False

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app


app = create_app()
app.secret_key = '123123123'


@app.route("/")
def home():
    form=MyForm()
    return render_template('index.html', form=form)

@app.route("/login", methods=['POST', 'GET'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if check_login_cred(login_form.email.data, login_form.password.data):
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)