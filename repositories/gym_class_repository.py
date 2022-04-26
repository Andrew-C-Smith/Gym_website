from db.run_sql import run_sql
from models.gym_class import *

def save(gym_class):
    sql = "INSERT INTO classes (name, date, time) VALUES (%s, %s, %s) RETURNING id"
    values = [gym_class.name, gym_class.date, gym_class.time]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_class.id = id


def select_all():
    classes = []
    sql = "SELECT * FROM classes"
    results = run_sql(sql)
    for result in results:
        gym_class = GymClass(result["name"], result["date"], result["time"], result["id"])
        classes.append(gym_class)
    return classes


def delete(id):
    sql = "DELETE FROM classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(gym_class):
    sql = "UPDATE classes SET name = %s WHERE id = %s"
    values = [gym_class.name, gym_class.date, gym_class.time]
    run_sql(sql, values)

def select(id):
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    gym_class = GymClass(result["name"], result["date"], result["time"], result["id"])
    return gym_class
