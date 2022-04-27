from db.run_sql import run_sql
from models.booking import Booking
from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repository
from models.user import User
import repositories.user_repository as user_repository

def save(booking):
    sql = "INSERT INTO bookings (user_id, classes_id) VALUES (%s, %s) RETURNING id"
    values = [booking.user.id, booking.gym_class.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id
    return booking


def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    gym_class = gym_class_repository.select(result["gym_class_id"])
    user = user_repository.select(result["user_id"])
    booking = Booking(user, gym_class, result["id"])
    print (booking)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        gym_class = gym_class_repository.select(result["classes_id"])
        user = user_repository.select(result["user_id"])
        booking = Booking(user, gym_class, result["id"])
        bookings.append(booking)
    return bookings