# Youtube video link:
# https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
# Learn making websites with Python


from flask import Flask, redirect, url_for

# Create an instance for our Flask application
app = Flask(__name__)


@app.route("/")
# app.route defines the path to our webpage
def home():
    return "<h1>This is the Home page<h1>"


@app.route("/<name>")
# app.route (<name>) Passes "name" as a parameter to the user function.
# E.g type nadeem like so http://127.0.0.1:5000/nadeem and nadeem gets
# passed to the function as an argument and stored in the name paremeter.
# Output would be "Hello nadeem"
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    # if you navigate to 127.0.0.1:5000/admin it will
    # redirect you to the home function.
    # To redirect admin to the user function.
    # name="Admin". passes admin to the user function
    return redirect(url_for("home", name="Admin"))


if __name__ == "__main__":
    # debug=True will run the web server every time you save a file.
    # Saves you having to stop/start it each time!
    app.run(debug=True)
