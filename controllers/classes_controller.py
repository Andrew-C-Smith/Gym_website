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