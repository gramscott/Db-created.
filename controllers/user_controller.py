from flask import Flask, render_template, request, redirect

from flask import Blueprint

users_blueprint = Blueprint("users", __name__)

import repositories.user_repository as user_repository

# import repositories.location_repository as location_repository

@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template ("users/index.html", users = users)

# NEW
# GET '/tasks/new'
@users_blueprint.route("/users/new", method =['GET'])
# CREATE
# POST '/tasks'

# SHOW
# GET '/tasks/<id>'

# EDIT
# GET '/tasks/<id>/edit'

# UPDATE
# PUT '/tasks/<id>'

# DELETE
# DELETE '/tasks/<id>'