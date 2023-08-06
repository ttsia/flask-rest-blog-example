from flask import Blueprint
from flask_restful import Api

from src.auth.views import LoginView, LogoutView, UserView

auth_bp = Blueprint("auth", __name__)
api = Api(auth_bp)

api.add_resource(UserView, "/api/users")
api.add_resource(LoginView, "/api/login")
api.add_resource(LogoutView, "/api/logout")
