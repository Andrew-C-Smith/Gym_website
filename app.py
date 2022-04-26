from flask import Flask, redirect, render_template, Blueprint

from controllers.classes_controller import classes_blueprint
from controllers.user_controller import users_blueprint


app = Flask(__name__)

app.register_blueprint(classes_blueprint)
app.register_blueprint(users_blueprint)

# @app.route("/")
# def main():
#     return render_template('index.html')

@app.route("/")
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('index.html', title='Home')

if __name__ == '__main__':
    app.run()