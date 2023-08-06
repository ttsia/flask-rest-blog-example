from flask import Flask
from flask_migrate import Migrate

from db import db
from settings import auth, current_config
from src.auth.routes import auth_bp
from src.blog.routes import blog_bp


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    Migrate(app, db)

    auth.JWT.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(blog_bp)

    return app


APP = create_app(current_config)

if __name__ == "__main__":
    APP.run()
