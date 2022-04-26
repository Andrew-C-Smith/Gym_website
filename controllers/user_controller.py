from flask import Blueprint, Flask, redirect, render_template, request

from models.gym_class import GymClass
from models.user import User
import repositories.gym_class_repository as gym_class_repository
import repositories.user_type_repository as user_type_repository
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

# INDEX
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/user_index.html", users=users)



# SHOW
@users_blueprint.route("/users/<id>")
def show_user(id):
    user = user_repository.select(id)
    return render_template("users/show.html", user=user)


# NEW
@users_blueprint.route("/users/user_new")
def new_user():
    user_types = user_type_repository.select_all()
    return render_template("users/user_new.html", user_types=user_types)



# CREATE
@users_blueprint.route("/users", methods=["POST"])
def create_user():
    name = request.form["name"]
    user_type_id = request.form["user_type_id"]
    user_type = user_type_repository.select(user_type_id)
    new_user = User(name, user_type)
    user_repository.save(new_user)
    return redirect("/users")


# DELETE
@users_blueprint.route("/users/<id>/delete", methods=["POST"])
def delete_user(id):
    user_repository.delete(id)
    return redirect("/users")

# EDIT
@users_blueprint.route("/users/<id>/edit")
def edit_user(id):
    user = user_repository.select(id)
    user_types = user_type_repository.select_all()
    return render_template('users/user_edit.html', user=user, user_types=user_types)


# UPDATE
@users_blueprint.route("/users/<id>", methods=["POST"])
def update_user(id):
    name = request.form["name"]
    user_type_id = request.form["user_type_id"]
    user_type = user_type_repository.select(user_type_id)
    user = User(name, user_type, id)
    user_repository.update(user)
    return redirect("/users")