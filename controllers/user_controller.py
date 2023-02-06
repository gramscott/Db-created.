from flask import Flask, render_template, request, redirect

from flask import Blueprint

import repositories.user_repository as user_repository


users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template ("users/index.html", users = users)

@users_blueprint.route("/users/<id>")
def show():
    user = user_repository.select_all(id)
    locations = user_repository.locations(user)
    return render_template("users/show.html", users=users, locations = locations)
