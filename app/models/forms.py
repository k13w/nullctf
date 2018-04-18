from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')

class FlagForm(FlaskForm):
    flag = StringField('flag', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('submit')

class addChallenge(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    category = StringField('category', validators=[DataRequired()])
    content = StringField('content', validators=[DataRequired()])
    flag = StringField('flag', validators=[DataRequired()])
    value = IntegerField('value', validators=[DataRequired()])
