import pdb

from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repository

from models.user import User
import repositories.user_repository as user_repository

from models.booking import Booking
import repositories.booking_repository as booking_repository

from models.user_type import UserType
import repositories.user_type_repository as user_type_repository

class_1 = GymClass('Kung Fu', '02 May, 2022', '07:00')
gym_class_repository.save(class_1)

class_2 = GymClass('Building jumps', '03 May, 2022', '07:00')
gym_class_repository.save(class_2)

class_3 = GymClass('Juijitsu', '04 May, 2022', '07:00')


user_type_1 = UserType('Admin')
user_type_repository.save(user_type_1)

user_type_2 = UserType('Member')
user_type_repository.save(user_type_2)


user_1 = User('Dozer', user_type_2)
user_repository.save(user_1)

user_2 = User('Neo', user_type_2)
user_repository.save(user_2)

booking_1 = Booking(user_2, class_2)
booking_repository.save(booking_1)

