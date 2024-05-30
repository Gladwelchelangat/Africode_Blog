from flask import Flask , render_template,url_for , flash,redirect
from form import RegistrationForm, LoginForm


app = Flask(__name__)
app.config["SECRET_KEY"] = '2c009f354f1be68ea912a649e631f15a'

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"account created for{form.username.data}!","success")
        return redirect(url_for('home'))
    return render_template("register.html", title="Register",form=form)


@app.route("/login")
def login():
    form =LoginForm()
    return render_template("login.html", title="Login",form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5009)