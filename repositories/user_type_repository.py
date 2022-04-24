from db.run_sql import run_sql
from models.user_type import UserType

def save(user_type):
    sql = "INSERT INTO user_types (name) VALUES (%s) RETURNING id"
    values = [user_type.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user_type.id = id