# from db.run_sql import run_sql 
# from models.user import User
# from models.location import Location 
# # import repositories.user_repository as user_repository


# def save(user):
#     sql = "INSERT INTO users (name, job) VALUES (%s, %s) RETURNING *"
#     values = [user.name, user.job]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     user.id = id
#     return user

# def select_all():
#     users = []

#     sql = "SELECT * FROM users"
#     results = run_sql(sql)

#     for row in results:
#         user = User(row['name'], row['job'], row['id'])
#         users.append(user)
#     return users

