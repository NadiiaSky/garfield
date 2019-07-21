import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = "this-really-needs-to-be-changed"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))


@app.route("/")
def hello_world():
    return "hello, garfield"


@app.route("/users")
def users():
    users = User.query.all()
    users_response = [
        {
            "id": user.id,
            "name": user.name
        } for user in users
    ]
    return jsonify(users_response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
