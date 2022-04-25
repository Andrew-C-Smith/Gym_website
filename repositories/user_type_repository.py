from db.run_sql import run_sql
from models.user_type import UserType

def save(user_type):
    sql = "INSERT INTO user_types (name) VALUES (%s) RETURNING id"
    values = [user_type.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user_type.id = id


def select(id):
    sql = "SELECT * FROM user_types WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    user_type = UserType(result["name"], result["id"])
    return user_type