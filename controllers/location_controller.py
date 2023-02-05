from flask import Flask,  render_template

from flask import Blueprint

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route("/locations")
def locations():
    return render_template("locations/index.html")