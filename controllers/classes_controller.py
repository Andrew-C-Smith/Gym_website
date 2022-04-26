from flask import Blueprint, Flask, redirect, render_template, request

from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repository
import repositories.user_type_repository as class_type_repository

classes_blueprint = Blueprint("classes", __name__)

# INDEX
@classes_blueprint.route("/classes")
def classes():
    classes = gym_class_repository.select_all()
    return render_template("classes/class_index.html", classes=classes)

# NEW
@classes_blueprint.route("/classes/class_new")
def new_class():
    return render_template("classes/class_new.html")


 # CREATE
@classes_blueprint.route("/classes", methods=["POST"])
def create_class():
    name = request.form["name"]
    date = request.form["date"]
    time = request.form["time"]
    new_class = GymClass(name, date, time)
    gym_class_repository.save(new_class)
    return redirect("/classes")


# EDIT
@classes_blueprint.route("/classes/<id>/edit")
def edit_class(id):
    classes = gym_class_repository.select(id)
    return render_template('classes/edit.html', classes=classes)


# UPDATE
@classes_blueprint.route("/classes/<id>", methods=["POST"])
def update_class(id):
    name = request.form["name"]
    gym_class = GymClass(name, id)
    gym_class_repository.update(gym_class)
    return redirect("/classes")


# DELETE
@classes_blueprint.route("/classes/<id>/delete", methods=["POST"])
def delete(id):
    gym_class_repository.delete(id)
    return redirect("/classes")