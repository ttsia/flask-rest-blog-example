from datetime import datetime
from typing import Any, Dict

from db import db


class Post(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(200), nullable=False)
    content: str = db.Column(db.Text, nullable=False)
    author_id: int = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    @classmethod
    def create(cls, title: str, content: str, author_id: int) -> "Post":
        post = cls(title=title, content=content, author_id=author_id)
        db.session.add(post)
        db.session.commit()
        return post

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author_id": self.author_id,
            "created_at": self.created_at.isoformat(),
        }


class Comment(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    content: str = db.Column(db.Text, nullable=False)
    author_id: int = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id: int = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    @classmethod
    def create(cls, content: str, post_id: int, author_id: int) -> "Comment":
        comment = cls(content=content, post_id=post_id, author_id=author_id)
        db.session.add(comment)
        db.session.commit()
        return comment

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "content": self.content,
            "author_id": self.author_id,
            "post_id": self.post_id,
            "created_at": self.created_at.isoformat(),
        }
