from db.run_sql import run_sql
from models.booking import Booking
from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repository
from models.user import User
import repositories.user_repository as user_repository

def save(booking):
    sql = "INSERT INTO bookings (gym_class_id, member_id) VALUES (%s, %s) RETURNING id"
    values = [booking.gym_class.id, booking.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id


def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    gym_class = gym_class_repository.select(result["gym_class_id"])
    user = user_repository.select(result["user_id"])
    biting = Booking(gym_class, user, result["id"])
    return biting