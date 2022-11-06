# Youtube video link:
# https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
# Learn Adding, Deleting and Updating Users in SQLAlchemy Database.


from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

# NOTE: SQLAlchemy allows you to save data using Python rather than writing SQL


app = Flask(__name__)
app.secret_key = "nadeemtest"
app.permanent_session_lifetime = timedelta(minutes=30)
# Setup DB configuration. Users is the table we will reference.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# Do not track all modification to the DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Create a database object
db = SQLAlchemy(app)


class users(db.Model):
    # Inherit db.Model which is a DB model and DB related methods.
    # id will be set as and integer value and as the primary key.
    _id = db.Column("id", db.Integer, primary_key=True)
    # Define DB column name, type and set max char length. E.g. 100, 6, etc.
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["username"]
        session["user"] = user

        # Query users class, filter by name and display the first entry found
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            # Pass user, email to the users class
            usr = users(user, "email")
            db.session.add(usr)
            db.session.commit()

        flash("Login successful")
        return redirect(url_for("user"))
    else:
        # Check if user already logged in. If so, redirect to user page.
        if "user" in session:
            flash("Redirected back to the user page. As you were already logged in")
            return redirect(url_for("user"))
        else:
            return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You've been logged out", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


@app.route("/user", methods=["GET", "POST"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Your details have been saved to the database")
        else:
            # Get email from session data
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))


@app.route("/view")
def view():
    # Function used to view information in the database
    return render_template("view.html", values=users.query.all())


if __name__ == "__main__":
    # Create the database using the "users" class
    with app.app_context():
        db.create_all()
        app.run(host="127.0.0.1", port=5001, debug=True)
