from flask import Flask,  render_template

from flask import Blueprint

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/users")
def locations():
    return render_template("users/index.html")