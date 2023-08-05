from flask import (
    Flask,
    render_template,
    redirect,
)  # Import Flask to allow us to create our app

app = Flask(__name__)  # Create a new instance of the Flask class called "app"


@app.route("/")
def index():
    return redirect("/play")


@app.route("/play")
def play():
    num = 3
    color = "blue"
    return render_template("index.html", num=num, color=color)


@app.route("/play/<int:num>")
def play_num(num):
    color = "blue"
    return render_template("index.html", num=num, color=color)


@app.route("/play/<int:num>/<string:color>")
def colorcall(num, color):
    return render_template("index.html", num=num, color=color)


# @app.route("/Dojo")
# def dojo():
#     return "Dojo"


# @app.route("/say/<name>")
# def say(name):
#     return "Hi, " + name


# @app.route("/repeat/<int:num>/<string:word>")
# def repeat(num, word):
#     output = ""
#     for i in range(0, num):
#         output += f"<p>{word}</p>"
#     return output


if (
    __name__ == "__main__"
):  # Ensure this file is being run directly and not from a different module
    app.run(debug=True, host="localhost", port=8002)  # Run the app in debug mode.
