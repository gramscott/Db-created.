from flask import Flask,  render_template, redirect, request

from flask import Blueprint

from models.location import Location

import repositories.location_repository as location_repository

import repositories.user_repository as user_repository 
import pdb

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route("/locations")
def locations():
    locations = location_repository.select_all()
    return render_template("locations/index.html", locations=locations)


@locations_blueprint.route("/locations/<id>", methods=['POST'])
def update(id):
    # pdb.set_trace()
    user_id = request.form['user_id']
    # need location name
    name = request.form['name'] 
    # set name needed
    set = request.form['set']
    filmed = request.form['filmed']
    good_climate = request.form['good_climate']
    user = user_repository.select(request.form["user_id"])
    location = Location(name, user, set, filmed, good_climate, id)
    # pdb.set_trace()
    location_repository.update(location)
    return redirect('/locations')


@locations_blueprint.route("/locations/<id>", methods=['GET'])
def show(id):
    location = location_repository.select(id)
    # user = user_repository.select(location.user_id)
    return render_template("locations/show.html", location=location)


@locations_blueprint.route("/locations/new", methods=['GET'])
def new_location():
    users = user_repository.select_all()
    # pdb.set_trace()
    # location = location_repository.select_all()
    return render_template("locations/new.html", users = users)

@locations_blueprint.route("/locations", methods = ['POST'])
def create_location():
    user_id = request.form['user_id']
    name = request.form['name']
    set = request.form['set']
    filmed = request.form['filmed']
    good_climate = request.form['good_climate']
    user = user_repository.select(user_id)
    location = Location(name, user, set, filmed, good_climate)
    # pdb.set_trace()
    location_repository.save(location)
    return redirect('/locations')


@locations_blueprint.route("/locations/<id>/delete", methods = ['POST'])
def delete_location(id):
    location_repository.delete(id)
    return redirect('/locations')


@locations_blueprint.route("/locations/<id>/edit", methods = ['GET'])
def edit_location(id):
    location = location_repository.select(id)
    users = user_repository.select_all()
    return render_template('locations/edit.html', location=location, users = users)