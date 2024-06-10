
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask 
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv



load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = '2c009f354f1be68ea912a649e631f15a'
app.config["SQLALCHEMY_DATABASE_URI"] ='sqlite:///site.db'
db =SQLAlchemy(app)
bcrypt =Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="login"
login_manager.login_message_category="info"
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'chelangatgladwel9@gmail.com'
app.config['MAIL_PASSWORD'] = 'kidd knzx sylk okbv'
mail = Mail(app)

from app import route