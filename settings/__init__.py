import os

from settings.develop import DevelopConfig

config = {
    "development": DevelopConfig,
}

config_name = os.environ.get("FLASK_ENV", "development")
current_config = config[config_name]
