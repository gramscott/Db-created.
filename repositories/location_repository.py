from db.run_sql import run_sql

from models.location import Location

from models.user import User

import repositories.user_repository as user_repository 

def save(location):
    sql = "INSERT INTO locations (name, set, filmed, good_climate, user_id) VALUES  (%s, %s, %s, %s, %s) RETURNING *"
    values = [location.name, location.set, location.filmed, location.good_climate, location.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id
    return location


def select_all():
    locations = []

    sql = "SELECT * FROM locations"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        location = Location(row['name'], user, row['set'], row['filmed'], row['good_climate'], row['id'])
        locations.append(location)
    return locations

def select(id):
    location = None 
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = user_repository.select(result['user_id'])
        location = Location(result['name'], user, result['set'], result['filmed'], result['good_climate'], result['id'])
    return location

def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(location):
    sql = "UPDATE locations SET(name, set, filmed, good_climate, user_id) = (%s,  %s, %s, %s, %s) WHERE id = %s"
    values = [location.name, location.set, location.filmed, location.good_climate, location.id]
    run_sql(sql, values)

