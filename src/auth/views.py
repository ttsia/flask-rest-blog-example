from typing import Any, Dict

from flask import abort, jsonify
from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse

from settings.auth import BLACKLIST
from src.auth.models import User
from db import db

class UserView(Resource):
    def post(self) -> Dict[str, Any]:
        parser = reqparse.RequestParser()
        parser.add_argument(
            "username", type=str, required=True, help="Username cannot be blank"
        )
        parser.add_argument(
            "email", type=str, required=True, help="Email cannot be blank"
        )
        parser.add_argument(
            "password", type=str, required=True, help="Password cannot be blank"
        )
        args = parser.parse_args()

        # Check if a user with the given email already exists
        existing_user = User.query.filter_by(email=args["email"]).first()
        if existing_user:
            abort(409)

        user = User.create(
            username=args["username"], email=args["email"], password=args["password"]
        )

        return {"message": "User registration successful", "data": user.to_dict()}

    @jwt_required()
    def get(self) -> Dict[str, Any]:
        user_id = get_jwt_identity()
        user = db.session.get(User, user_id)
        if not user:
            abort(404)
        return {"data": user.to_dict()}


class LoginView(Resource):
    def post(self) -> Dict[str, Any]:
        parser = reqparse.RequestParser()
        parser.add_argument(
            "email", type=str, required=True, help="Email cannot be blank"
        )
        parser.add_argument(
            "password", type=str, required=True, help="Password cannot be blank"
        )
        args = parser.parse_args()

        user = User.query.filter_by(email=args["email"]).first()
        if not user or not user.verify_password(args["password"]):
            abort(401)

        token = user.generate_auth_token()

        return {"message": "User login successful", "token": token}


class LogoutView(Resource):
    @jwt_required()
    def post(self) -> Dict[str, str]:
        BLACKLIST.add(get_jwt()["jti"])
        return {"message": "Successfully logged out"}
