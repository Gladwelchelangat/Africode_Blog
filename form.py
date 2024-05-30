from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegistrationForm(FlaskForm):
    username =StringField('Username', validators=[DataRequired(), Length(min=4,max=12)])
    email =StringField('Email' , validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[Length(min=4,max=12), DataRequired() ])
    confirm_password =PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    submit =SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email =StringField('Email' , validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember =BooleanField('Remember me')
    submit =SubmitField('Login')
 
