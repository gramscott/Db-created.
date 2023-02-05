from db.run_sql import run_sql 
from models.user import User
from models.location import Location 
import repositories.location_repository as location_repository


def save(location):
    sql = "INSERT INTO location(name, set, filmed, good_climate) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [location.name, location.set, location.filmed, location.good_climate]
    results = run_sql(sql, values)
    location.id = results[0]['id']
    return location

def select_all():
    locations = []

    sql = 'SELECT * FROM locations'
    results = run_sql(sql)

    for row in results:
        location = Location(row['name'], row['set'], row['filmed'], row['good_climate'], row['id'])
        locations.append(location)
    return locations



