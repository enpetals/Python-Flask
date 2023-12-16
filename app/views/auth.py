from flask import Blueprint, render_template, request, redirect, flash, session
from ..utils.helper import find_item_in_list
from ..utils.decorators import authenticate,guest


auth = Blueprint("auth", __name__)

# sesssions are used to store user related information on the server. informations stored in a session is accessible anywher in
# the application

users = []


@auth.get("/")
@guest
def login_page():
    return render_template("login.html")


@auth.get("/register")
@guest
def register_page():
    return render_template("register.html")


@auth.post("/create")
def create_user():
    form = request.form

    users.append(form)
    print("users", users)

    return redirect("/auth")


@auth.post("/login")
def login_user():

    form = request.form
    existing_user = None

    print("FORM:", form)
    # CKECK IF USER EXIXTS
    for user in users:
        if user.get("email") == form.get("email"):
            existing_user = user

    if not existing_user:
        flash("user does not exist")
        return redirect("/auth")

    # CHECK THE PASSWORD
    if existing_user.get("password") != form.get("password"):
        flash("incorect credentials")
        return redirect("/auth")

    # CREATE USER
    session["LOGGED_USER"] = existing_user.get("email")

    # REDIRECT TO DASHBOARD
    return redirect("/auth/dashboard")


@auth.get("/dashboard")
@authenticate
def dashboard_page():
    def get_logged_user(value, index, array):
        email = session.get("LOGGED_USER")
        print("EMAIL:", email)
        return value.get("email") == email

    user = find_item_in_list(users, get_logged_user)
    return render_template("dashboard.html", user=user)


auth.get("/test")
@authenticate
def test_page_route():
    return "test"


@auth.get("/logout")
def logout_user():
    # session.clear()
    session.pop("LOGGED_USER")
    return redirect("/auth")
