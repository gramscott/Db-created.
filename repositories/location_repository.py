# from db.run_sql import run_sql 
# from models.user import User
# from models.location import Location 
# import repositories.location_repository as location_repository
# import repositories.user_repository as user_repository




# def save(location):
#     sql = "INSERT INTO locations (name, set, filmed, good_climate, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
#     values = [location.name, location.set, location.filmed, location.good_climate, location.user.id]
#     results = run_sql(sql, values)
#     location.id = results[0]['id']
#     location.id = id
#     return location



# def select_all():
#     locations = []
    
#     sql = 'SELECT * FROM locations'
#     results = run_sql(sql)
    
#     for row in results:
#         user = user_repository.select(row['user_id'])
#         location = Location(row['name'], user, row['set'], row['filmed'], row['good_climate'], row['id'])
#         locations.append(location)
#     return locations 



