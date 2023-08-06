from typing import Any, Dict, List

from flask import abort
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse

from src.blog.models import Post, Comment
from db import db

class PostsView(Resource):
    @jwt_required()
    def get(self) -> Dict[str, List[Dict[str, Any]]]:
        posts = Post.query.all()
        return {"data": [post.to_dict() for post in posts]}

    @jwt_required()
    def post(self) -> Dict[str, Any]:
        parser = reqparse.RequestParser()
        parser.add_argument(
            "title", type=str, required=True, help="Title cannot be blank"
        )
        parser.add_argument(
            "content", type=str, required=True, help="Content cannot be blank"
        )
        args = parser.parse_args()
        user_id = get_jwt_identity()

        post = Post.create(
            title=args["title"], content=args["content"], author_id=user_id
        )

        return {"message": "Blog post created successfully", "data": post.to_dict()}


class PostDetailsView(Resource):
    @jwt_required()
    def get(self, post_id: int) -> Dict[str, Any]:
        post = db.session.get(Post, post_id)
        if not post:
            abort(404)
        return {"data": post.to_dict()}


class CommentsView(Resource):
    @jwt_required()
    def post(self, post_id: int) -> Dict[str, Any]:
        parser = reqparse.RequestParser()
        parser.add_argument(
            "content", type=str, required=True, help="Content cannot be blank"
        )
        args = parser.parse_args()

        post = db.session.get(Post, post_id)
        if not post:
            abort(404)

        comment = Comment.create(
            content=args["content"], post_id=post_id, author_id=get_jwt_identity()
        )

        return {
            "message": f"Added comment to blog post with ID {post_id}",
            "data": comment.to_dict(),
        }

    @jwt_required()
    def get(self, post_id: int) -> Dict[str, List[Dict[str, Any]]]:
        post = db.session.get(Post, post_id)
        if not post:
            abort(404)

        post_comments = Comment.query.filter_by(post_id=post_id).all()
        return {"data": [comment.to_dict() for comment in post_comments]}
