# Youtube video link:
# https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
# Learn making HTML templates


from flask import Flask, render_template

# Create an instance for our Flask applicationMain
app = Flask(__name__)


@app.route("/<name>")
# app.route defines the path to our webpages
def home(name):
    # Render the index.html page. Pass the value of content=name to it.
    return render_template("index.html", content=["Nadeem", "Tim", "Susan"])


if __name__ == "__main__":
    # debug=True will run the web server every time you save a file.
    # Saves you having to stop/start it each time!
    app.run(debug=True)
