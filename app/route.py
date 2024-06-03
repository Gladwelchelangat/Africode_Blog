from flask import render_template,url_for,redirect,flash,request
from app import app,bcrypt,db
from app.form import RegistrationForm,LoginForm
from app.models import User
from flask_login import login_user,logout_user,current_user,login_required


posts=[
    {"author":"Gladwel chelangat",
"title":"blog post 1",
"content":"information",
"date_posted":"May 27, 2024"},
      {"author":"Naomi Cherono",
"title":"blog post 2",
"content":"information",
"date_posted":"May 27, 2024"},
      {"author":"Enock Bett",
"title":"blog post 3", 
"content":"information",
"date_posted":"May 27, 2024"}
]

@app.route("/")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["POST","GET"])
def register():
    if current_user.is_authenticated:
         return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password =bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user =User(username=form.username.data,email=form.email.data,password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created. You may now login!","success")
        return redirect(url_for('login'))
    return render_template("register.html", title="Register",form=form)


@app.route("/login", methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
         return redirect(url_for("home"))
    form =LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
             login_user(user,remember=form.remember.data)
             next_page=request.args.get('next')
                
        return redirect(next_page) if next else redirect(url_for("home"))

         
             
    
    else:
            flash("Login Unsuccessful,please check username and password",'danger')

    return render_template("login.html", title="Login",form=form)

@app.route("/log_out")
def log_out():
     logout_user()
     return redirect(url_for("home"))

@app.route("/account")
@login_required
def account():
     return render_template('account.html',tittle=account)





