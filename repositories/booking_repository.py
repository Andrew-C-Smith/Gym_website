from db.run_sql import run_sql
from models.booking import Booking
from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repository
from models.user import User
import repositories.user_repository as user_repository

def save(biting):
    sql = "INSERT INTO bookings (gym_class_id, member_id) VALUES (%s, %s) RETURNING id"
    values = [booking.gym_class.id, booking.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    biting.id = id