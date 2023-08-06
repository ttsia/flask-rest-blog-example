from flask import Blueprint
from flask_restful import Api

from .views import CommentsView, PostDetailsView, PostsView

blog_bp = Blueprint("blog", __name__)
api = Api(blog_bp)

api.add_resource(PostDetailsView, "/api/posts/<int:post_id>")
api.add_resource(CommentsView, "/api/posts/<int:post_id>/comments")
api.add_resource(PostsView, "/api/posts")
