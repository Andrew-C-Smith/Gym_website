from db.run_sql import run_sql
from models.booking import Booking
from models.user import User
from models.user_type import UserType
import repositories.user_type_repository as user_type_repository
import repositories.user_repository as user_repository

def save(user):
    sql = "INSERT INTO users (name, user_type_id) VALUES (%s, %s) RETURNING id"
    values = [user.name, user.user_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    print(results[0])
    user.id = id

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for result in results:
        
        user = User(result["name"], result["id"])
        users.append(user)
    return users
    

