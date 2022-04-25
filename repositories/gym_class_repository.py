from db.run_sql import run_sql
from models.gym_class import *

def save(gym_class):
    sql = "INSERT INTO classes (name, date, time) VALUES (%s, %s, %s) RETURNING id"
    values = [gym_class.name, gym_class.date, gym_class.time]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_class.id = id
