from typing import Any, Dict

import bcrypt
from flask_jwt_extended import create_access_token

from db import db


class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(50), unique=True, nullable=False)
    email: str = db.Column(db.String(100), unique=True, nullable=False)
    password_hash: str = db.Column(db.String(100), nullable=False)

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.set_password(password)

    @classmethod
    def create(cls, username: str, email: str, password: str) -> "User":
        user = cls(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def set_password(self, password: str) -> None:
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode("utf-8"), salt).decode(
            "utf-8"
        )

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(
            password.encode("utf-8"), self.password_hash.encode("utf-8")
        )

    def generate_auth_token(self) -> str:
        return create_access_token(identity=self.id)

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "username": self.username, "email": self.email}
