from flask import Blueprint, render_template,request,redirect
from forms import UserForm
from auth_models import User
from flask_login import login_user
auth_app = Blueprint('auth_app', __name__,
                     template_folder='templates')



@auth_app.route("/login",methods=["GET","POST"])
def login():
    form = UserForm()
    if request.method == "POST":
        form_data = request.form
        user = User.query\
               .filter(User.login==form_data.get("login"))\
               .filter(User.password==form_data.get("password"))\
               .first()
        if user:
            login_user(user)
            return redirect("/admin")
        
    return render_template("login.html",form=form)
