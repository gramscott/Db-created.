from flask import Flask,  render_template, redirect, request

from flask import Blueprint

from models.location import Location

import repositories.location_repository as location_repository

import repositories.user_repository as user_repository 

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route("/locations")
def locations():
    locations = location_repository.select_all()
    return render_template("locations/index.html", locations=locations)

@locations_blueprint.route("/locations/<id>")
def show(id):
    location = location_repository.select(id)
    users = location_repository.users(location)
    return render_template("location/show.html", location=location, users=users)

# @locations_blueprint("/locations/new", methods=['GET'])
# def new_location():
#     users = user_repository.select_all()
#     locations = location_repository.select_all()
#     return render_template("locations.new.html", users = users, locations = locations)

@locations_blueprint.route("/locations", methods = ['POST'])
def create_location():
    user_id = request.form['user_id']
    name = request.form['name']
    set = request.form['filmed']
    good_climate = request.form['good_climate']
    location = Location(user_id, name, set, good_climate)
    location_repository.save(location)
    return redirect('/locations')


@locations_blueprint.route("/locations/<id>/delete", methods = ['POST'])
def delete_location(id):
    location_repository.delete(id)
    return redirect('/locations')
