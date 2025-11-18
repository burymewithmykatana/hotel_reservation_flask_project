from flask import Flask, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson import ObjectId
from wtforms import Form, StringField, EmailField, IntegerField, validators
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)
from os.path import isdir
from os import mkdir, getcwd
from datetime import datetime

# ------------------ DB CONNECTION ------------------ #

client = MongoClient("localhost", 27017)
db = client["hotelDB"]
userCollection = db["users"]
roleCollection = db["roles"]
roomCollection = db["rooms"]
reservationCollection = db["reservations"]


# ------------------ INITIAL DATA ------------------ #

def rolePopulate():
    """
    Populate roles and create an initial manager user if DB is empty.
    Roles: manager, staff, guest
    """
    # TODO: Check if roles collection is empty, then insert 3 roles
    # TODO: Create default manager user with role "manager"
    pass


# ------------------ FORMS / VALIDATORS ------------------ #

class UserForm(Form):
    name = StringField("Name", validators=[validators.DataRequired()])
    family = StringField("Family", validators=[validators.DataRequired()])
    email = EmailField("Email", validators=[validators.DataRequired(), validators.Email()])
    password = StringField("Password", validators=[validators.DataRequired(), validators.Length(min=6, max=32)])


class RoomForm(Form):
    name = StringField("Name", validators=[validators.DataRequired(), validators.Length(min=2, max=50)])
    type = StringField("Type", validators=[validators.DataRequired()])  # e.g. single, double, suite
    capacity = IntegerField("Capacity", validators=[validators.DataRequired(), validators.NumberRange(min=1, max=10)])
    price_per_night = IntegerField("Price", validators=[validators.DataRequired(), validators.NumberRange(min=1)])


class ReservationForm(Form):
    room_id = StringField("Room ID", validators=[validators.DataRequired()])
    start_date = StringField("Start Date (YYYY-MM-DD)", validators=[validators.DataRequired()])
    end_date = StringField("End Date (YYYY-MM-DD)", validators=[validators.DataRequired()])


# ------------------ FILE UPLOAD UTIL ------------------ #

def saveFile(file):
    """
    Save uploaded file into /public folder.
    Return dict with {message, savingPath, status}
    """
    # TODO: Implement similar to your original saveFile
    # - Create /public if not exists
    # - Save file there
    # - Return path & status
    return {"message": "Not implemented yet", "status": 400}


# ------------------ RESOURCES ------------------ #

class Signup(Resource):
    def post(self):
        """
        Public: sign up as a guest user.
        - Validate form
        - Set role to 'guest'
        - Insert into users collection
        """
        # TODO
        return {"message": "Signup not implemented yet"}, 501


class Login(Resource):
    def post(self):
        """
        Public: login with email + password
        - Check user
        - Create JWT with role_name in claims
        """
        # TODO
        return {"message": "Login not implemented yet"}, 501


class Users(Resource):
    @jwt_required()
    def get(self):
        """
        Manager only:
        - Read role from token
        - If manager, return paginated list of users
        """
        # TODO
        return {"message": "Users list not implemented yet"}, 501


class Rooms(Resource):
    def get(self, id=None):
        """
        Public:
        - If no id: return paginated list of rooms
        - If id: return single room
        """
        # TODO
        return {"message": "Get rooms not implemented yet"}, 501

    @jwt_required()
    def post(self):
        """
        staff/manager:
        - Validate room data with RoomForm
        - Handle image upload
        - Insert into roomCollection
        """
        # TODO
        return {"message": "Create room not implemented yet"}, 501

    @jwt_required()
    def put(self, id=None):
        """
        staff/manager:
        - Update room data
        """
        # TODO
        return {"message": "Update room not implemented yet"}, 501

    @jwt_required()
    def delete(self, id=None):
        """
        manager only:
        - Delete room
        """
        # TODO
        return {"message": "Delete room not implemented yet"}, 501


class Reservations(Resource):
    @jwt_required()
    def get(self, id=None):
        """
        - guest: only their own reservations
        - staff/manager: see all reservations
        - Optional: pagination
        """
        # TODO
        return {"message": "Get reservations not implemented yet"}, 501

    @jwt_required()
    def post(self):
        """
        Create reservation:
        - Validate with ReservationForm
        - Check room exists
        - Calculate total_price = nights * price_per_night
        - (Optional) prevent overlapping reservations for same room
        """
        # TODO
        return {"message": "Create reservation not implemented yet"}, 501

    @jwt_required()
    def put(self, id=None):
        """
        staff/manager:
        - Update reservation dates
        """
        # TODO
        return {"message": "Update reservation not implemented yet"}, 501

    @jwt_required()
    def delete(self, id=None):
        """
        manager only:
        - Delete reservation
        """
        # TODO
        return {"message": "Delete reservation not implemented yet"}, 501


# ------------------ APP FACTORY ------------------ #

def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "hotelSecret"
    jwt = JWTManager(app)

    # Routes
    api.add_resource(Signup, "/signup")
    api.add_resource(Login, "/login")
    api.add_resource(Users, "/users")
    api.add_resource(Rooms, "/rooms", "/rooms/<string:id>")
    api.add_resource(Reservations, "/reservations", "/reservations/<string:id>")

    # Init data
    rolePopulate()

    return app


def main():
    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
