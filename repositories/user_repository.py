from db.run_sql import run_sql 
from models.user import User
from models.location import Location 
import repositories.user_repository as user_repository


def save(user):
    sql = "INSERT INTO users (name, job) VALUES (%s, %s) RETURNING id"
    values = [user.name, user.job]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id



def select_all():
    users = []

    sql = 'SELECT * FROM users'
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['id'])
        users.append(user)
    return users


def select(id):
    user = None
    sql = 'SELECT * FROM users WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        user = User(result['name'], result['job'], result['id'] )
    return user


 
