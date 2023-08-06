import pytest

from app import create_app, db
from settings.test import TestConfig
from src.auth.models import User
from src.blog.models import Post, Comment


@pytest.fixture(scope="module")
def test_app():
    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="module")
def client(test_app):
    return test_app.test_client()


@pytest.fixture()
def create_user():
    def _create_user(username, email, password):
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    return _create_user


@pytest.fixture()
def create_post():
    def _create_post(title, content, author_id):
        post = Post(title=title, content=content, author_id=author_id)
        db.session.add(post)
        db.session.commit()
        return post

    return _create_post


@pytest.fixture()
def create_comment():
    def _create_comment(content, author_id, post_id):
        comment = Comment(content=content, author_id=author_id, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        return comment

    return _create_comment


@pytest.fixture()
def user(create_user):
    user = create_user("testuser", "test@example.com", "password123")
    return user


@pytest.fixture()
def test_post(user, create_post):
    post = create_post("test", "test", user.id)
    return post


@pytest.fixture(autouse=True)
def clean_up_database(test_app):
    with test_app.app_context():
        db.session.remove()
        db.drop_all()
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()
