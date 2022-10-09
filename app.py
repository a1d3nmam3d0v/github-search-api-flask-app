from flask import Flask, render_template, request  # NOT the same as requests
from github_api import get_github_user

app = Flask(__name__)


@app.route("/")  # homepage
def homepage():
    return render_template("index.html")


@app.route("/get_user")
def get_user_info():
    # get user info from github api, display on page
    print("form data is", request.args)
    username = request.args.get("username")  # safer - returns None if no username
    # username = requests.args["username"]  # more common but errors if no username
    user_info, error_message = get_github_user(username)  # user_info is a  dictionary
    if error_message:
        return render_template("error.html", error=error_message)
    else:
        return render_template("github.html", user_info=user_info)


if __name__ == "__main__":
    app.run()
