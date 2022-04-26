from flask import Blueprint, Flask, redirect, render_template, request

from models.gym_class import GymClass
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.user_type_repository as user_type_repository
import repositories.user_repository as user_repository

bookings_blueprint = Blueprint("bookings", __name__)

# INDEX
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/booking_index.html", booking=bookings)


# NEW
@bookings_blueprint.route("/bookings/new")
def new_booking():
    gym_classes = gym_class_repository.select_all()
    users = user_repository.select_all()
    return render_template("bookings/booking_new.html", gym_class=gym_classes, user=users)


# CREATE
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    gym_class_id = request.form["gym_class_id"]
    user_id = request.form["user_id"]
    gym_class = gym_class_repository.select(gym_class_id)
    user = user_repository.select(user_id)
    new_booking = Booking(gym_class, user)
    booking_repository.save(new_booking)
    return redirect("/bookings")


# EDIT
@bookings_blueprint.route("/bookings/<id>/edit")
def edit_ooking(id):
    booking = booking_repository.select(id)
    gym_classes = gym_class_repository.select_all()
    users = user_repository.select_all()
    return render_template('bookings/booking_edit.html', booking=booking, gym_classes=gym_classes, users=users)


# UPDATE
@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    gym_class_id = request.form["gym_class_id"]
    user_id = request.form["user_id"]
    gym_class = gym_class_repository.select(gym_class_id)
    user = user_repository.select(user_id)
    booking = Booking(gym_class, user, id)
    booking_repository.update(booking)
    return redirect("/bookings")


# DELETE
@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")
