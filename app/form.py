from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from app.models import User
from flask_login import current_user
from flask_wtf.file import FileField,FileAllowed


class RegistrationForm(FlaskForm):
    username =StringField('Username', validators=[DataRequired(), Length(min=4,max=12)])
    email =StringField('Email' , validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[Length(min=4,max=12), DataRequired() ])
    confirm_password =PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    submit =SubmitField('Sign Up')

    def validate_username(self,username):
        user =User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken .please choose a different one.')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken .please choose a different one.')   


class LoginForm(FlaskForm):
    email = StringField('Email' , validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember =BooleanField('Remember me')
    submit =SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username =StringField('Username', validators=[DataRequired(), Length(min=4,max=12)])
    email =StringField('Email' , validators=[DataRequired(), Email()])
    picture=FileField('picture',validators=[FileAllowed(['jpg','jpeg','png'])])

    submit =SubmitField('update')

    def validate_username(self,username):
        if username.data !=current_user.username:
           
           user =User.query.filter_by(username=username.data).first()
           if user:
               raise ValidationError('That username is taken .please choose a different one.')

    def validate_email(self,email):
        if email.data !=current_user.email:
           user =User.query.filter_by(email=email.data).first()
           if user:
               raise ValidationError('That email is taken .please choose a different one.')

class PostForm(FlaskForm):
    title=StringField('title',validators=[DataRequired()])
    content=TextAreaField('content',validators=[DataRequired()])
    submit=SubmitField('Post')
 


class RequestResetForm(FlaskForm):
    
    email =StringField('Email' , validators=[DataRequired(), Email()])
  
    submit =SubmitField('request password reset')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email.')  

class ResetPasswordForm(FlaskForm):
    password = PasswordField('password', validators=[Length(min=4,max=12), DataRequired() ])
    confirm_password =PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    submit =SubmitField('reset password')

